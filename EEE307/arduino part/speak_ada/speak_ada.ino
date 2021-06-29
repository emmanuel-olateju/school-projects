#include <digitalWriteFast.h>
#include <Talkie.h>
#include <TalkieUtils.h>
#include <Vocab_Soundbites.h>
#include <Vocab_Special.h>
#include <Vocab_Toms_Diner.h>
#include <Vocab_US_Acorn.h>
#include <Vocab_US_Clock.h>
#include <Vocab_US_Large.h>
#include <Vocab_US_TI99.h>
Talkie ola;

#define permit 12
#define pwd 7
#define fng 10
#define conf 9
#define enter 8

void setup() {
  pinMode(permit,INPUT);
  pinMode(pwd,INPUT);
  pinMode(fng,INPUT);
  pinMode(conf,INPUT);
  pinMode(enter,INPUT);
  #define permits digitalRead(permit)
  #define pwds digitalRead(pwd)
  #define fngs digitalRead(fng)
  #define confs digitalRead(conf)
  #define enters digitalRead(enter)
}

void loop() {
  if(enters==HIGH){
    ola.say(sp2_ENTER);
    delay(900);
  }
  if((pwds==HIGH) and (confs==HIGH)){
    ola.say(sp4_AFFIRMATIVE);
    delay(1900);  
  }
  if((pwds==HIGH) and (confs==LOW)){
    ola.say(sp4_NEGATIVE);
    delay(900);  
  }
  if((fngs==HIGH) and (confs==HIGH)){
    ola.say(sp4_AFFIRMATIVE);
    delay(1900); 
  }
  if((fngs==HIGH) and (confs==LOW)){
    ola.say(sp4_FAILURE);
    delay(900);   
  }
  if((permits==HIGH) and (confs==HIGH)){
    ola.say(sp4_OPEN);
    delay(900);  
  }
  if((permits==HIGH) and (confs==LOW)){
    ola.say(sp4_SECURITY);
    delay(900);  
  }
}
