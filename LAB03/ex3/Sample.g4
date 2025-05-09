grammar Sample;

program : (command | conditionalCommand)+ PUNCT? EOF;

command : playAction | turnAction | setAction | increaseAction | decreaseAction;

conditionalCommand : 'if' condition 'then' command;

condition : 'the' 'time' 'is' comparator timeExpression;

comparator : 'after' | 'before' | 'at';

playAction : 'play' playValidObject location?;
turnAction : 'turn' turnModifier article? turnOnValidObject;
setAction : 'set' setValidObject 'to' INT;
increaseAction : 'increase' increaseValidObject 'by' INT;
decreaseAction : 'decrease' increaseValidObject 'by' INT;

turnModifier : 'on' | 'off';

playValidObject : 'music' | 'song' | 'alarm' | 'video';
turnOnValidObject : 'light' | 'fan' | locationPhrase 'light' | locationPhrase 'lamp';
setValidObject : 'temperature';
increaseValidObject : 'brightness' | 'volume' | 'temperature';

timeExpression : hourMinuteTime | specificTime;

hourMinuteTime : INT ':' INT;
specificTime : 'morning' | 'afternoon' | 'evening' | 'night';

location : 'in' article? locationPhrase;

article : 'the' | 'a' | 'an';

locationPhrase : WORD (WORD)*;

WORD : [a-zA-Z]+;
INT : [0-9]+;
PUNCT : [!.?];
WS : [ \t\r\n]+ -> skip;