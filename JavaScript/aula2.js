class Pessoa{
    nome;
    peso;
    altura;

    constructor(nome,peso,altura) {
        this.nome = nome;
        this.peso = peso;
        this.altura = altura;
    }

    calcularImc(){
        return this.peso/(this.altura * this.altura);
    }

    classsificarImc(){
        const imc = this.calcularImc();
        if (imc > 20) {
            return ('seu imc esta acima de '+ imc);
        } else {
            return ('vai comer');
        }
    }
}


const jose = new Pessoa ('Jose', 70, 1.75);
console.log(jose.calcularImc(),jose.classsificarImc());

