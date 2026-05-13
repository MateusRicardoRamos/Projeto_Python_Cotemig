from flask import Flask

app = Flask(__name__) 

@app.route('/decorator') 
def decorator():
    return 'Um decorator (decorador) em Python é uma funcionalidade poderosa e elegante que permite modificar, estender ou envolver o comportamento de funções, métodos ou classes sem alterar o seu código-fonte original.Funcionalmente, um decorator é uma função que recebe outra função como argumento, adiciona alguma funcionalidade e retorna uma nova função, geralmente com o comportamento modificado.' 

if __name__ == '__main__':
    app.run(debug=True)