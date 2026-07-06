from django.db import models

# Create your models here.

class users(models.Model):
	name=models.CharField(max_length=159);
	email=models.CharField(max_length=159);
	pass_word=models.CharField(max_length=159);
	phone=models.CharField(max_length=159);
	city=models.CharField(max_length=159);
	gender=models.CharField(max_length=159);
	
class manufacturers(models.Model):
	name=models.CharField(max_length=159);
	email=models.CharField(max_length=159);
	pass_word=models.CharField(max_length=159);
	city=models.CharField(max_length=159);
	address=models.CharField(max_length=159);
	stz=models.CharField(max_length=159);

class pharmacies(models.Model):
	name=models.CharField(max_length=159);
	email=models.CharField(max_length=159);
	pass_word=models.CharField(max_length=159);
	city=models.CharField(max_length=159);
	address=models.CharField(max_length=159);
	phone=models.CharField(max_length=159);


class drug(models.Model):
	did=models.CharField(max_length=159, primary_key = True);
	drugname=models.CharField(max_length=159);
	mname=models.CharField(max_length=159);
	typ_e=models.CharField(max_length=159);
	uses=models.CharField(max_length=159);
	instructions=models.CharField(max_length=159);
	cost=models.FloatField();
	mrp=models.FloatField();
	cname=models.CharField(max_length=159);
	cemail=models.CharField(max_length=159);
	stock=models.FloatField();
	

class drugstock_p(models.Model):
	did=models.CharField(max_length=159);
	drugname=models.CharField(max_length=159);
	mname=models.CharField(max_length=159);
	typ_e=models.CharField(max_length=159);
	uses=models.CharField(max_length=159);
	instructions=models.CharField(max_length=159);
	cost=models.FloatField();
	mrp=models.FloatField();
	pname=models.CharField(max_length=159);
	pemail=models.CharField(max_length=159);
	stock=models.IntegerField();

class cart_p(models.Model):
	did=models.CharField(max_length=159);
	mname=models.CharField(max_length=159);
	totcost=models.FloatField();
	count=models.IntegerField();
	pemail=models.CharField(max_length=159);

class cart_u(models.Model):
	did=models.CharField(max_length=159);
	drugname=models.CharField(max_length=159);
	mname=models.CharField(max_length=159);
	cost=models.FloatField();
	totcost=models.FloatField();
	count=models.IntegerField();
	
	pharmacy=models.CharField(max_length=159);
	pemail=models.CharField(max_length=159);
	
	email=models.CharField(max_length=159);

	stz=models.CharField(max_length=159);




	

	


