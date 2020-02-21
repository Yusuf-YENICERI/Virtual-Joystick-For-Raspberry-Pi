from kivy.uix.scatter import Scatter
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class BaseScatter(Widget):
	
	counter = 0
	centerPos = None
	
	def __init__(self, **kwargs):
		super(BaseScatter, self).__init__(**kwargs)
		print(self.center)
	
	def resetPos(self, touch):
		touch.center = self.center
		self.curLabel.text = "x: " + str(int(touch.x)) + ", y: " + str(int(touch.y))
	
	def showPos(self, touch):
		self.curLabel.text = "x: " + str(int(touch.x)) + ", y: " + str(int(touch.y))
	
	def tempPos(self, touch):
		self.curLabel.text = "x: " + str(int(touch.x)) + ", y: " + str(int(touch.y)) 

class BaseSubScatter(Widget):
	pass
	
class MyScatter(Scatter):
	def __init__(self, **kwargs):
		super(MyScatter, self).__init__(**kwargs)
	
		
class CurrentPosLabel(Label):
	pass


class ScatterApp(App):
    def build(self):
        s = BaseScatter()
        return s


ScatterApp().run()
