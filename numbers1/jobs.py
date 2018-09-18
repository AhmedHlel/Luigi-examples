import luigi
from random import randint
class Numbers(luigi.Task):
 
	def requires(self):
		return []
 
	def output(self):
		return luigi.LocalTarget("numbers.txt")
 
	def run(self):
		with self.output().open('w') as f:
			for i in range(1, 6):
				number = randint(0, 9)
				f.write("{}\n".format(number))
 
class Letters(luigi.Task):
 
	def requires(self):
		return [Numbers()]
 
	def output(self):
		return luigi.LocalTarget("letters.txt")
 
	def run(self):

		dict_  = {"0":"Zero","1":"One", "2":"Two", "3":"Three", "4": "Four", "5": "Five", "6":"Six", "7":"Seven", "8":"Eight", "9": "Nine", "10":"Ten"}
		with self.input()[0].open() as fin, self.output().open('w') as fout:
			for line in fin:
				n = line.strip()
				out = dict_[n]
				fout.write("{}:{}\n".format(n, out))
				 
if __name__ == '__main__':
	luigi.run()
