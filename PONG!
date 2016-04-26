# Implementation of classic arcade game Pong

import pygame
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
##import simpleguitk as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos=paddle2_pos=150
paddle1_vel=paddle2_vel=0
score1=score2=0
paddle_len=70
max_score=2
x=True
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[300,200]
    if direction==RIGHT:
        ball_vel=[random.randrange(120,240)/60,-random.randrange(60,120)/60]
    if direction==LEFT:
        ball_vel=[-random.randrange(120,240)/60,-random.randrange(60,120)/60]

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, x  # these are numbers
    global score1, score2  # these are ints
    x=True
    score1=score2=0
    paddle1_pos=paddle2_pos=150
    paddle1_vel=paddle2_vel=0
    spawn_ball(RIGHT)
    
def restart():
    new_game()
    
def draw(canvas):
    global x
    if x:    
        global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel


        # draw mid line and gutters
        canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
        canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
        canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

        # update ball
        if ball_pos[0]<=BALL_RADIUS+PAD_WIDTH+1 and not(ball_pos[1] in range(paddle1_pos,paddle1_pos+paddle_len)):
            spawn_ball(RIGHT)
            score2+=1
        if score2==max_score:
            x=False
        if ball_pos[0]>=WIDTH-BALL_RADIUS-PAD_WIDTH-1 and not(ball_pos[1] in range(paddle2_pos,paddle2_pos+paddle_len)):
            spawn_ball(LEFT)
            score1+=1
        if score1==max_score:
            x=False
        if ball_pos[1]<=BALL_RADIUS+1:
            ball_vel[1]=-ball_vel[1]
            ball_pos[1]+=ball_vel[1]
        if ball_pos[1]>=HEIGHT-BALL_RADIUS-1:
            ball_vel[1]=-ball_vel[1]
            ball_pos[1]+=ball_vel[1]
        ball_pos[0]+=ball_vel[0]
        ball_pos[1]+=ball_vel[1]

        # draw ball

        canvas.draw_circle(ball_pos,BALL_RADIUS,1,"White","White")

        # update paddle's vertical position, keep paddle on the screen

        if (paddle1_pos<=0 and paddle1_vel>0) or(paddle1_pos>=HEIGHT-paddle_len and paddle1_vel<0) or paddle1_pos in range(1,HEIGHT-paddle_len):
            paddle1_pos+=paddle1_vel
        if (paddle2_pos<=0 and paddle2_vel>0) or(paddle2_pos>=HEIGHT-paddle_len and paddle2_vel<0) or paddle2_pos in range(1,HEIGHT-paddle_len):
            paddle2_pos+=paddle2_vel

        # draw paddles

        canvas.draw_line([PAD_WIDTH/2,paddle1_pos],[PAD_WIDTH/2,paddle1_pos+paddle_len],PAD_WIDTH,'Blue')
        canvas.draw_line([WIDTH-PAD_WIDTH/2,paddle2_pos],[WIDTH-PAD_WIDTH/2,paddle2_pos+paddle_len],PAD_WIDTH,'Blue')

        # determine whether paddle and ball collide    
        if ball_pos[0]<=BALL_RADIUS+PAD_WIDTH+1 and ball_pos[1] in range(paddle1_pos,paddle1_pos+paddle_len):
            ball_vel[0]=-1.3*ball_vel[0]
            ball_pos[0]+=ball_vel[0]
        if ball_pos[0]>=WIDTH-BALL_RADIUS-PAD_WIDTH-1 and ball_pos[1] in range(paddle2_pos,paddle2_pos+paddle_len):
            ball_vel[0]=-1.3*ball_vel[0]
            ball_pos[0]+=ball_vel[0]

        # draw scores
        canvas.draw_text(str(score1),[200,30],40,"White")
        canvas.draw_text(str(score2),[400,30],40,"White")
    else:
        if score1==max_score:
            canvas.draw_text("player1 won",[200,150],60,"White")
        if score2==max_score:
            canvas.draw_text("player2 won",[200,150],60,"White")

def inc_pad():
    global paddle_len
    if paddle_len<=120:
        paddle_len+=10

def dec_pad():
    global paddle_len
    if paddle_len>=40:
        paddle_len-=10

def inc_ball_rad():
    global BALL_RADIUS
    if BALL_RADIUS<=50:
        BALL_RADIUS+=5

def dec_ball_rad():
    global BALL_RADIUS
    if BALL_RADIUS>=10:
        BALL_RADIUS-=5

def max_sco(maxscore):
    global max_score
    max_score=int(maxscore)
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP['up']:
        paddle2_vel=-10    
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel=10    
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel=-10    
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel=10    

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP['up']: 
        paddle2_vel=0    
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel=0    
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel=0    
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel=0    
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("RESTART",restart,150)
frame.add_label("                    ")
frame.add_button("INCREASE PADDLE LENGTH",inc_pad,150)
frame.add_label("                    ")
frame.add_button("DECREASE PADDLE LENGTH",dec_pad,150)
frame.add_label("                    ")
frame.add_button("ENLARGE PONG",inc_ball_rad,150)
frame.add_label("                    ")
frame.add_button("SHORTEN PONG",dec_ball_rad,150)
frame.add_label("                    ")
frame.add_input("max point",max_sco,100)
# start frame
new_game()
frame.start()
