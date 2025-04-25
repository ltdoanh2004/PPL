grammar Sample;

command: simpleCommand | conditionalCommand;

simpleCommand: action deviceObject modifier?;

conditionalCommand: 'If' condition 'then' simpleCommand;

action: VERB PREPOSITION? ;

deviceObject: lightDevice | temperatureDevice | musicDevice | brightnessDevice;

lightDevice: 'the' WORD* 'light';
temperatureDevice: 'the' WORD* 'temperature';
musicDevice: 'music' ('in' | 'in' 'the') WORD+;
brightnessDevice: 'brightness';

modifier: ('by' | 'to') INT;

condition: timeCondition;

timeCondition: 'the' 'time' 'is' comparator time;

VERB: 'Turn' | 'Set' | 'Increase' | 'Decrease' | 'Play';

PREPOSITION: 'on' | 'off' | 'up' | 'down';

WORD: [a-zA-Z]+;

time: INT ':' INT;

comparator: 'before' | 'after' | 'at' ;

INT: [0-9]+;

WS: [ \t\r\n]+ -> skip;