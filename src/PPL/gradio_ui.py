import gradio as gr
from poem_dsl_parser import parse_poem_command, TOPIC_DESCRIPTIONS

def format_help():
    """Format help message for chatbot"""
    return """Tôi có thể giúp bạn tạo thơ tiếng Việt. Bạn có thể:

1. Tạo thơ thông thường:
   - Gõ: "tạo thơ"
   - Tôi sẽ hướng dẫn bạn nhập:
     + Model ID (số >= 0)
     + Context (text)
     + Số khổ thơ (số > 0)

2. Tạo thơ có chủ đề:
   - Gõ: "tạo thơ chủ đề"
   - Tôi sẽ hướng dẫn bạn nhập:
     + Context (text)
     + Chọn chủ đề (0-4)

3. Xem danh sách chủ đề:
   - Gõ: "danh sách chủ đề"

4. Xem thông tin model:
   - Gõ: "thông tin model"

5. Xem hướng dẫn:
   - Gõ: "hướng dẫn"

Bạn muốn thử chức năng nào?"""

def format_topics():
    """Format topics message for chatbot"""
    topics = "Danh sách các chủ đề có sẵn:\n\n"
    for topic_id, description in TOPIC_DESCRIPTIONS.items():
        topics += f"{topic_id}: {description}\n"
    return topics

def format_model_info():
    """Format model info message for chatbot"""
    return """Thông tin về các model:

1. Model thông thường (PoemGenerator):
   - Sinh thơ dựa trên context và số khổ
   - Không giới hạn chủ đề
   - Có thể chọn model_id khác nhau

2. Model có chủ đề (ControlledPoemGenerator):
   - Sinh thơ theo chủ đề cụ thể
   - 5 chủ đề có sẵn:
     + 0: Gia Đình
     + 1: Tình Yêu
     + 2: Dịch Bệnh
     + 3: Quê Hương
     + 4: Lễ Tết
   - Tối ưu cho từng chủ đề"""

def generate_poem_command(model_id, context, n_stanzas):
    """Generate a regular poem command"""
    return f'GENERATE POEM MODEL {model_id} CONTEXT "{context}" STANZAS {n_stanzas}'

def generate_controlled_poem_command(context, topic_id):
    """Generate a controlled poem command"""
    return f'GENERATE CONTROLLED POEM CONTEXT "{context}" TOPIC {topic_id}'

def format_poem_for_markdown(poem: str) -> str:
    # Đảm bảo mỗi khổ cách nhau 1 dòng trắng (4 dòng 1 khổ)
    lines = poem.strip().split('\n')
    stanzas = []
    stanza = []
    for i, line in enumerate(lines):
        stanza.append(line)
        if (i + 1) % 4 == 0:
            stanzas.append('\n'.join(stanza))
            stanza = []
    if stanza:
        stanzas.append('\n'.join(stanza))
    return '\n\n'.join(stanzas)

def chat(message, history):
    """Handle chat messages"""
    history = history or []
    message = message.lower().strip()
    
    if message == "hướng dẫn":
        return format_help(), history + [(message, format_help())]
    
    elif message == "danh sách chủ đề":
        topics = format_topics()
        return topics, history + [(message, topics)]
    
    elif message == "thông tin model":
        info = format_model_info()
        return info, history + [(message, info)]
    
    elif message == "tạo thơ":
        response = """Vui lòng nhập thông tin theo định dạng:
model_id context \"nội dung\" số_khổ

Ví dụ:
0 \"ai ơi\" 2

Trong đó:
- model_id: số >= 0
- context: text trong dấu nháy kép
- số_khổ: số > 0"""
        return response, history + [(message, response)]
    
    elif message == "tạo thơ chủ đề":
        response = """Vui lòng nhập thông tin theo định dạng:
context \"nội dung\" topic_id

Ví dụ:
\"cha mẹ một nắng hai sương\" 0

Trong đó:
- context: text trong dấu nháy kép
- topic_id: số từ 0-4"""
        return response, history + [(message, response)]
    
    elif message.startswith(("0 ", "1 ", "2 ", "3 ", "4 ")):
        # Try to parse as poem generation command
        try:
            parts = message.split('"')
            if len(parts) == 3:  # Regular poem
                model_id = int(parts[0].strip())
                context = parts[1]
                n_stanzas = int(parts[2].strip())
                command = generate_poem_command(model_id, context, n_stanzas)
            else:  # Controlled poem
                context = parts[1]
                topic_id = int(parts[2].strip())
                command = generate_controlled_poem_command(context, topic_id)
            
            success, result = parse_poem_command(command)
            if success:
                # Nếu là thơ (nhiều dòng), tự động format lại cho rõ khổ
                if isinstance(result, str) and result.count('\n') > 3:
                    result = format_poem_for_markdown(result)
                return result, history + [(message, result)]
            else:
                return f"Lỗi: {result}", history + [(message, f"Lỗi: {result}")]
        except Exception as e:
            return f"Lỗi: Định dạng không đúng. Vui lòng nhập lại theo hướng dẫn.", history + [(message, f"Lỗi: Định dạng không đúng. Vui lòng nhập lại theo hướng dẫn.")]
    
    else:
        response = """Tôi không hiểu lệnh của bạn. Vui lòng gõ "hướng dẫn" để xem các lệnh có sẵn."""
        return response, history + [(message, response)]

def chat_and_clear(message, history):
    reply, updated_history = chat(message, history)
    return "", updated_history

# Create the Gradio interface
with gr.Blocks(title="Poem Generation Chatbot") as demo:
    gr.Markdown("# 🎭 Poem Generation Chatbot")
    gr.Markdown("Chat với tôi để tạo thơ tiếng Việt")

    chatbot = gr.Chatbot(
        label="Chat",
        height=600
    )
    msg = gr.Textbox(
        label="Nhập tin nhắn",
        placeholder="Gõ 'hướng dẫn' để xem các lệnh có sẵn...",
        lines=1
    )
    clear = gr.Button("Xóa chat")

    msg.submit(chat_and_clear, [msg, chatbot], [msg, chatbot], queue=False)
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch() 