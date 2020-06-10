class data:

	def convert(self,s):
		s = s.replace(',',"")
		if(s=="-"): return 0
		return float(s)



	def __init__(self):
		self.strikeprice=None
		self.calls_oi = None
		self.calls_change_in_oi = None
		self.calls_ltp = None
		self.puts_oi = None
		self.puts_change_in_oi = None
		self.puts_ltp = None


	def getdata(self,row):
		self.strikeprice = self.convert(row[11].text)
		self.calls_oi = self.convert(row[1].text)
		self.calls_change_in_oi = self.convert(row[2].text)
		self.calls_ltp = self.convert(row[5].text)
		self.puts_oi = self.convert(row[21].text)
		self.puts_change_in_oi = self.convert(row[20].text)
		self.puts_ltp = self.convert(row[17].text)

	def pr(self):
		print("calls oi:",self.calls_oi,"\ncalls chage in oi ",self.calls_change_in_oi,"\ncalls ltp ",self.calls_ltp,"\nstrike price ",self.strikeprice,"\nputs ltp ",self.puts_ltp,"\nputs change in oi ",self.puts_change_in_oi,"\nputs oi ",self.puts_oi,end="\n\n")

	def li(self,):
		t = [self.calls_oi,self.calls_change_in_oi,self.calls_ltp,self.strikeprice,self.puts_oi,self.puts_change_in_oi,self.puts_ltp]
		return t