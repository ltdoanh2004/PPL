grammar Sample;

command:  simpleCommand | conditionalCommand;

simpleCommand: action deviceObject modifier?;
conditionalCommand: 'If' condition 'then' simpleCommand;

action: 'Turn' 'on' | 'Turn' 'off' | 'Set' | 'Increase' | 'Decrease' | 'Play';

deviceObject: ('the' roomName? 'light') | ('the' roomName? 'temperature') | ('music' 'in' roomName) | 'brightness';

roomName: 'kitchen' | 'living room' | 'bedroom' | 'bathroom' | 'office';

modifier: 'by' INT | 'to' INT;

condition: 'the' 'time' 'is' 'after' time;

time: INT ':' INT;

INT: [0-9]+;

WS: [ \t\r\n]+ -> skip;
