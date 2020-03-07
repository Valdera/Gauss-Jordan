from gaussJordan import gaussjordan
from flask import Flask, request, render_template

app = Flask(__name__)
app.secret_key = 'gaussjordan'

@app.route('/', methods=['GET','POST'])
def index():
	if (request.method == 'GET'):
		return render_template('index.html')
	elif (request.method == 'POST'):
		linear_mtx = list()
		solution = list()
		cnt = int(request.form['count'])
		for i in range(cnt):
			tmp = list()
			for j in range(cnt):
				tmp.append(int(request.form['mi'+str(i)+'j'+str(j)]))
			linear_mtx.append(tmp)
		for i in range(cnt):
			solution.append(int(request.form['mi'+str(i)+'j'+str(cnt)]))
		linear_mtx, solution = gaussjordan(linear_mtx,solution)
		return render_template('result.html', mtx = linear_mtx, sol = solution, count = cnt)

if (__name__ == '__main__'):
	app.run()
