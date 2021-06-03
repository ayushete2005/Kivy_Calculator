from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core import text
from kivy.core.window import Window

Builder.load_file('design.kv')


Window.size = (350,450)
class MyLayout(Widget):
	def clear(self):
		self.ids.input.text = '0'
	
	def digit(self, value):
		prior = self.ids.input.text
		if prior == "ERROR":
			prior = ""

		# print((prior.endswith("*") or prior.endswith("/")))
		# print((value == "-" or value == "+"))
		if (prior.endswith("*") or prior.endswith("*"))  and (value == "-" or value == "+"):
			prior = f"{prior}{value}"
			self.ids.input.text = prior
		if value == "-" or value == "+" or value == "*" or value == "/":
			if prior.endswith("+") or prior.endswith("-") or prior.endswith("*") or prior.endswith("/"):return 0
		if prior == "0" :
			prior = "" 
		self.ids.input.text = prior + value
	
	def dot(self):
		prior = self.ids.input.text
		if prior == "ERROR":
			prior = ""
		list = prior.split("+")
		
		if  "." not in list[-1]:
			prior = f'{prior}.'
			self.ids.input.text = prior 

	
	def Result(self):
		try:
			prior = self.ids.input.text
			# print(prior)
			prior = prior.replace("%","/100")
			# print(type(prior))
			# print(eval(self.ids.input.text))
			answer = eval(prior)

			'''
			#Addition
			if "+" in prior:
				list = prior.split("+")
				prior = 0
				for letter in range(0, len(list)):
					print(letter)
					prior = prior + float(list[letter])
					print(prior)
			'''

			self.ids.input.text = str(answer)
		except:
			self.ids.input.text = "ERROR"

	def Backspace(self):
		prior = self.ids.input.text
		if prior == "ERROR":
			prior = ""
		prior = prior[:-1]
		self.ids.input.text = prior




		
		 


class app(App):
	def build(self):
		# Window.clearcolor = (1,1,1,1)
		return MyLayout()

if __name__ == '__main__':
	app().run()