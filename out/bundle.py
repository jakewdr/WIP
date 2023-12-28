PK    `[�W�Ɉ�       cfg.pyc���
    �[�e�   �                   �   � d dl mZ d� ZdS )�    )�Dictc                 �   � t          | d�  �        5 }t          d� d� |D �   �         D �   �         �  �        cd d d �  �         S # 1 swxY w Y   d S )N�rc                 �:   � g | ]}|�                     d d�  �        ��S )�=�   )�split��.0�lines     �
out/cfg.py�
<listcomp>zunpackCfg.<locals>.<listcomp>   s&   � �2y�2y�2y��4�:�:�c�!�3D�3D�2y�2y�2y�    c                 �8   � g | ]}|�                     d �  �        ��S )�
)�stripr
   s     r   r   zunpackCfg.<locals>.<listcomp>   s)   � �Ox�Ox�Ox�dh�PT�PZ�PZ�[_�P`�P`�Ox�Ox�Oxr   )�open�dict)�cfgFile�cfgContentss     r   �	unpackCfgr      sv   � �
�7�3���z�+�T�2y�2y�Ox�Ox�lw�Ox�Ox�Ox�2y�2y�2y�-z�-z�z�z�z�z�z�z�z�z�z�z�z�z����z�z�z�z�z�zs   �#A�A�AN)�typingr   r   � r   r   �<module>r      s5   �� � � � � � �{� {� {� {� {r   PK    `[�W��a�"       decoder.pyc���
    �[�e  �                   �0   � d dl Z d dlZd dlmZ 	 d� Zd� ZdS )�    N)�BytesIOc                 �p  � t          | d�  �        5 }t          t          j        t	          t          j        |�                    �   �         �  �        �  �        d�  �        �                    |�  �        �                    d�  �        �  �        �	                    dd�  �        cd d d �  �         S # 1 swxY w Y   d S )N�rb�rzUTF-8�� )
�open�str�zipfile�ZipFiler   �base64�	b64decode�read�decode�replace��pakFilePath�filePath�pakFiles      �out/decoder.py�decodeTextFiler      s  � �
�;�t���  b�w�c�'�/�'�&�JZ�[b�[g�[g�[i�[i�Jj�Jj�Bk�Bk�lo�2p�2p�2u�2u�v~�2�2�  3G�  3G�  HO�  3P�  3P�  /Q�  /Q�  /Y�  /Y�  Z^�  _a�  /b�  /b�  b�  b�  b�  b�  b�  b�  b�  b�  b�  b�  b�  b����  b�  b�  b�  b�  b�  bs   �BB+�+B/�2B/c                 �"  � t          | d�  �        5 }t          t          j        t          t	          j        |�                    �   �         �  �        �  �        d�  �        �                    |�  �        �  �        cd d d �  �         S # 1 swxY w Y   d S )Nr   r   )r	   r   r   r   r   r   r   r   s      r   �decodeImageFiler      s�   � �
�;�t���  E�w�g�g�o�g�f�N^�_f�_k�_k�_m�_m�Nn�Nn�Fo�Fo�ps�6t�6t�6y�6y�  {C�  7D�  7D�  /E�  /E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E����  E�  E�  E�  E�  E�  Es   �A&B�B�B)r   r   �ior   r   r   � �    r   �<module>r      sb   �� � � � � � � � � � � � � � � p�b� b� b�E� E� E� E� Er   PK    `[�W��/  *  
   engine.pyc*���
    �[�e-   �                   �   � d � Z dS )c                  �$   � t          d�  �         d S )NzGame engine connected :p)�print� �    �out/engine.py�checkr      s   � �E�,�-�-�-�-�-r   N)r   r   r   r   �<module>r      s   �� -� -� -� -� -r   PK    `[�W͂��-  (     game.pyc(���
    �[�e-   �                   �   � d � Z dS )c                  �$   � t          d�  �         d S )NzGame window connected :p)�print� �    �out/game.py�checkr      s   � �E�,�-�-�-�-�-r   N)r   r   r   r   �<module>r      s   �� -� -� -� -� -r   PK    `[�W�.΢�  �     __main__.py�D�_A='image'
import decoder,pygame,random,cfg,sys,os,game,engine
game.check()
engine.check()
scriptPath=str(os.path.realpath(__file__).replace(os.sep,'/'))
bundlePath=scriptPath.replace('/__main__.py','')
containingFolder=scriptPath.replace('bundle.py/__main__.py','')
WIDTH,HEIGHT=1080,720
FPS=60
WHITE=255,255,255
RED=255,0,0
GREEN=0,255,0
BLUE=0,0,255
BLACK=0,0,0
coloursConfig=cfg.unpackCfg(containingFolder+'colours.cfg')
BACKGROUNDCOLOUR=coloursConfig.get('background')
LINECOLOUR=coloursConfig.get('line')
WALLCOLOUR=coloursConfig.get('walls')
del coloursConfig
class Collisions:
	def wall_collision(entity):
		wall_rebound_acc=.83
		if entity.rect.left<room_rect.left:entity.rect.left=room_rect.left;entity.velocity[0]*=-1*wall_rebound_acc
		if entity.rect.right>room_rect.right:entity.rect.right=room_rect.right;entity.velocity[0]*=-1*wall_rebound_acc
		if entity.rect.top<room_rect.top:entity.rect.top=room_rect.top;entity.velocity[1]*=-1*wall_rebound_acc
		if entity.rect.bottom>room_rect.bottom:entity.rect.bottom=room_rect.bottom;entity.velocity[1]*=-1*wall_rebound_acc
	def resolve_collision(entity1,entity2,direction):
		_entity_rebound_acc=.83
		if entity2.velocity[direction]!=0 and entity1.velocity[direction]/entity2.velocity[direction]<0:entity1.velocity[direction]*=-1*_entity_rebound_acc;entity2.velocity[direction]*=-1*_entity_rebound_acc
		elif abs(entity1.velocity[direction])<abs(entity2.velocity[direction]):entity1.velocity[direction]*=1/_entity_rebound_acc;entity2.velocity[direction]*=-1*_entity_rebound_acc
		else:entity1.velocity[direction]*=-1*_entity_rebound_acc;entity2.velocity[direction]*=1/_entity_rebound_acc
	def entity_collision_check(entity1,entity2):
		if min(abs(entity1.rect.left-entity2.rect.right),abs(entity1.rect.right-entity2.rect.left))<min(abs(entity1.rect.top-entity2.rect.bottom),abs(entity1.rect.bottom-entity2.rect.top)):entity1.rect.center=entity1.previousCoordinates;Collisions.resolve_collision(entity1,entity2,0)
		if min(abs(entity1.rect.left-entity2.rect.right),abs(entity1.rect.right-entity2.rect.left))>min(abs(entity1.rect.top-entity2.rect.bottom),abs(entity1.rect.bottom-entity2.rect.top)):entity1.rect.center=entity1.previousCoordinates;Collisions.resolve_collision(entity1,entity2,1)
		if min(abs(entity1.rect.left-entity2.rect.right),abs(entity1.rect.right-entity2.rect.left))==min(abs(entity1.rect.top-entity2.rect.bottom),abs(entity1.rect.bottom-entity2.rect.top)):entity1.rect.center=entity1.previousCoordinates
	def entity_collision(entity1,entities):
		_entity_rebound_acc=.83;entities=list(entities);entities.pop(entities.index(entity1))
		for entity2 in entities:
			if entity1.lastCollided.count(entity2)==0 and entity1.rect.colliderect(entity2):Collisions.entity_collision_check(entity1,entity2);entity1.lastCollided.append(entity2);entity2.lastCollided.append(entity1)
			elif entity1.lastCollided.count(entity2)>0 and not entity1.rect.colliderect(entity2):entity1.lastCollided.remove(entity2)
class Entity:
	def __init__(self,x,y,width,height,imageMode,color,image):
		self.rect=pygame.Rect(x,y,width,height);self.velocity=[.0,.0];self.lastCollided=[];self.line_end=None;self.line_exists=False;self.imageMode=imageMode;self.previousCoordinates=self.rect.center
		if self.imageMode=='color':self.color=color
		elif self.imageMode==_A:self.image=pygame.image.load(image);self.image=pygame.transform.scale(self.image,(width,height))
	def apply_gravity(self):self.velocity[1]+=.5
	def apply_air_res(self):air_res=.998;self.velocity[0]*=air_res;self.velocity[1]*=air_res
	def accelerate_along_line(self):
		if self.line_exists and self.line_end:direction_vector=pygame.math.Vector2(self.line_end[0]-self.rect.centerx,self.line_end[1]-self.rect.centery+.1);distance=direction_vector.length();direction_vector=direction_vector.normalize();base_acceleration=-5.5;scaled_acceleration=distance*(WIDTH**2+HEIGHT**2)**.5*10**base_acceleration;self.velocity[0]+=direction_vector.x*scaled_acceleration;self.velocity[1]+=direction_vector.y*scaled_acceleration
	def random_swing(self,player):_random_x=random.randint(0,WIDTH);_random_y=random.randint(0,HEIGHT);self.line_end=player.rect.center;self.line_exists=True
	def update(self,entities):self.previousCoordinates=self.rect.center;self.rect.x+=self.velocity[0];self.rect.y+=self.velocity[1];self.apply_gravity();self.apply_air_res();Collisions.wall_collision(self);Collisions.entity_collision(self,entities)
	def draw(self,screen,imageMode):
		if imageMode=='color':pygame.draw.rect(screen,self.color,self.rect)
		elif imageMode==_A:screen.blit(self.image,self.rect)
		if self.line_exists and self.line_end:line_start=self.rect.centerx,self.rect.centery;pygame.draw.line(screen,LINECOLOUR,line_start,self.line_end,4)
class Wall:
	def __init__(self,x,y,width,height):self.rect=pygame.Rect(x,y,width,height);self.image=pygame.Surface((width,height));self.image.fill(BLACK)
	def draw(self,screen):pygame.draw.rect(screen,RED,self.rect)
def main():
	A='assets/Template.pak';print(os.getcwd());global room_rect;wall=Wall(WIDTH//2-4000,HEIGHT//2-200,40,200);screen=pygame.display.set_mode((WIDTH,HEIGHT));pygame.display.set_caption('Torsion-alphatest');Yakuza=decoder.decodeImageFile(containingFolder+A,'images/y6.png');Neco=decoder.decodeImageFile(containingFolder+A,'images/neco.png');player=Entity(70,70,50,50,_A,BLUE,Yakuza);third_entity=Entity(95,300,50,50,_A,RED,Neco);entities=[player,third_entity];room_rect=pygame.Rect(50,50,WIDTH-100,HEIGHT-100)
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:pygame.quit();sys.exit()
			elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:player.line_end=pygame.mouse.get_pos();player.line_exists=not player.line_exists
			if event.type==pygame.MOUSEBUTTONDOWN and event.button==3:third_entity.random_swing(player)
		for entity in entities:
			entity.accelerate_along_line();entity.update(entities)
			if entity.rect.colliderect(wall.rect):entity.velocity[0]*=-1;entity.velocity[1]*=-1
		screen.fill(BACKGROUNDCOLOUR);pygame.draw.rect(screen,WALLCOLOUR,room_rect,2);wall.draw(screen);[entity.draw(screen,entity.imageMode)for entity in entities];pygame.display.flip();pygame.time.wait(int(1000/FPS))
if __name__=='__main__':pygame.init();clock=pygame.time.Clock();main()PK     `[�W�Ɉ�               ��    cfg.pycPK     `[�W��a�"               ��2  decoder.pycPK     `[�W��/  *  
           ��}  engine.pycPK     `[�W͂��-  (             ���  game.pycPK     `[�W�.΢�  �             ��'  __main__.pyPK        '    