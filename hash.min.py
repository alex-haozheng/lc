import click
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives.serialization import Encoding,load_pem_private_key,load_pem_public_key,NoEncryption,PrivateFormat,PublicFormat
@click.group()
def B():
 pass
@click.command("generate-key")
@click.option("--output","-o",required=True)
def j(output:str):
 D=rsa.generate_private_key(public_exponent=65537,key_size=2048)
 H=D.private_bytes(Encoding.PEM,PrivateFormat.TraditionalOpenSSL,NoEncryption())
 with open(output,"wb")as f:
  f.write(H)
@click.command("output-public")
@click.option("--secret-key","-s",required=True)
@click.option("--output","-o",required=True)
def Y(secret_key:str,output:str):
 with open(secret_key,"rb")as f:
  H=f.read()
  try:
   D=load_pem_private_key(H,None)
  except:
   raise "Invalid secret key data"
 R=D.public_key()
 H=R.public_bytes(Encoding.PEM,PublicFormat.SubjectPublicKeyInfo)
 with open(output,"wb")as f:
  f.write(H)
@click.command("encrypt")
@click.option("--public-key","-p",required=True)
@click.option("--file","-f",required=True)
@click.option("--output","-o",required=True)
def k(public_key:str,file:str,output:str):
 with open(public_key,"rb")as f:
  H=f.read()
  try:
   pk=load_pem_public_key(H)
  except:
   raise "Invalid public key data"
 with open(file,"rb")as f:
  I=f.read()
  s=pk.encrypt(I,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
  with open(output,"wb")as f:
   f.write(s)
@click.command("decrypt")
@click.option("--secret-key","-s",required=True)
@click.option("--file","-f",required=True)
@click.option("--output","-o",required=True)
def O(secret_key:str,file:str,output:str):
 with open(secret_key,"rb")as f:
  H=f.read()
  try:
   D=load_pem_private_key(H,None)
  except:
   raise "Invalid secret key data"
 with open(file,"rb")as f:
  I=f.read()
  m=D.decrypt(I,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
  with open(output,"wb")as f:
   f.write(m)
B.add_command(j)
B.add_command(Y)
B.add_command(k)
B.add_command(O)
if __name__=="__main__":
 B()