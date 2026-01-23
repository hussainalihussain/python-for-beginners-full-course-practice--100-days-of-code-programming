f = open('my-db.txt', 'a')

n = '\n'

def writeToDb(message):
  f.write('* ' + message + n)

writeToDb('sameer')
writeToDb('junaid')
writeToDb('kamil')
writeToDb('afsar khan')