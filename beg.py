#erasthsones
def primes(n): # simple Sieve of Eratosthenes 
	odds = range(3, n+1, 2)
	sieve = set(sum([list(range(q*q, n+1, q+q)) for q in odds],[]))
	return [2] + [p for p in odds if p not in sieve]

def getEle(protons):
	elements_dic = dict([(1,'H'), (2,'He'), (3,'Li'),(4,'Be'),(5,'B'),(6,'C'),(7,'N'),(8,'O'),(9,'F'),(10,'Ne'),(11,'Na'),(12,'Mg'),(13,'Al'),(14,'Si'),(15,'P'),(16,'S'),(17,'Cl'),(18,'Ar'),(19,'K'),(20,'Ca'),(21,'Sc'),(22,'Ti'),(23,'V'),(24,'Cr'),(25,'Mn'),(26,'Fe'),(27,'Co'),(28,'Ni'),(29,'Cu'),(30,'Zn'),(31,'Ga'),(32,'Ge'),(33,'As'),(34,'Se'),(35,'Br'),(36,'Kr'),(37,'Rb'),(38,'Sr'),(39,'Y'),(40,'Zr'),(41,'Nb'),(42,'Mo'),(43,'Tc'),(44,'Ru'),(45,'Rh'),(46,'Pd'),(47,'Ag'),(48,'Cd'),(49,'In'),(50,'Sn'),(51,'Sb'),(52,'Te'),(53,'I'),(54,'Xe'),(55,'Cs'),(56,'Ba'),(57,'La'),(58,'Ce'),(59,'Pr'),(60,'Nd'),(61,'Pm'),(62,'Sm'),(63,'Eu'),(64,'Gd'),(65,'Tb'),(66,'Dy'),(67,'Ho'),(68,'Er'),(69,'Tm'),(70,'Yb'),(71,'Lu'),(72,'Hf'),(73,'Ta'),(74,'W'),(75,'Re'),(76,'Os'),(77,'Ir'),(78,'Pt'),(79,'Au'),(80,'Hg'),(81,'Tl'),(82,'Pb'),(83,'Bi'),(84,'Po'),(85,'At'),(86,'Rn'),(87,'Fr'),(88,'Ra'),(89,'Ac'),(90,'Th'),(91,'Pa'),(92,'U'),(93,'Mp'),(94,'Pu'),(95,'Am'),(96,'Cm'),(97,'Bk'),(98,'Cf'),(99,'Es'),(100,'Fm'),(101,'Md'),(102,'No'),(103,'Lr'),(104,'Rf'),(105,'Db'),(106,'Sg'),(107,'Bh'),(108,'Hs'),(109,'Mt'),(110,'Ds'),(111,'Rg'),(112,'Cn'),(113,'Nh'),(114,'Fl'),(115,'Mc'),(116,'Lv'),(117,'Ts'),(118,'Og')])
	
	ele = 'Err'
	for k,v in elements_dic.items():
		if k == protons:
			ele = v
	
	if ele == 'Err':
		ele = 'null'
		
	return ele
	
hstart = int(input('Where Shall H Start? 1-? '))
toend = int(input('Where does it end? '))

	
	
#make list
data_list = []
ctl_num = 1
prots = 1
p_ele = []

while ctl_num < hstart:
	rlist =[ctl_num, '-' , '-']
	data_list.append(rlist)
	ctl_num = ctl_num + 1
#build list

if hstart == 1:
	elem = 0
	elem = getEle(prots)
	tl = []
	tl = [ctl_num,prots,elem]
	print('Num: {0}, Prots: {1}, Element: {2}'.format(ctl_num,prots,elem))
	data_list.append(tl)
	prots = prots + 1
	ctl_num = ctl_num + 1
	
while ctl_num >= hstart and ctl_num <= toend:
	
	elem = 0
	elem = getEle(prots)
	tl = []
	
	
	if prots in primes(prots):
		tl = (ctl_num,prots,elem)
		p_ele.append(tl)
		tl = []

	if ctl_num in primes(ctl_num): #set testing conditional
		
		tl = [ctl_num, prots, elem]
		print('Num: {0}, Prots: {1}, Element: {2}'.format(ctl_num,prots,elem))
		prots = prots + 1
		
	else:
		tl = [ctl_num]
		print('Num: {}'.format(ctl_num))

	data_list.append(tl)
	ctl_num = ctl_num + 1
	
for item in p_ele:
	print(item)
	
	
	
	
	


	
	
	
	