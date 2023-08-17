const {gets,print} = require('./funcoes-auxiliares');

const media = gets();

if (media < 5) {
    print('Reprovado');
} else if (media >= 5 && media < 7) {
    print('Recuperação');   
} else if (media <0 || media > 10 ) {
    print('Digite um numero valido');
} else  {
    print("Aprovado");
}