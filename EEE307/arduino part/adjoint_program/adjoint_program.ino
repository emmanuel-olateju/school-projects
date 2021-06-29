#include <LiquidCrystal.h>
#include <EEPROM.h>
#include <Adafruit_Fingerprint.h>
#include <SoftwareSerial.h>
#include <Key.h>
#include <Keypad.h>

//fingerprint init
LiquidCrystal lcd(31,33,35,37,39,41);
SoftwareSerial mySerial(10,11);
SoftwareSerial status(0,1);
Adafruit_Fingerprint finger=Adafruit_Fingerprint(&mySerial);
uint8_t id;
//keyad init
const byte ROWS=4;
const byte COLUMNS=4;
char keys[COLUMNS][ROWS]={
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte rowPins[ROWS]={9,8,7,6};
byte colPins[COLUMNS]={5,4,3,2};
Keypad customKeypad=Keypad(makeKeymap(keys),rowPins,colPins,ROWS,COLUMNS);

//access control parameters declaration
//inputs
int address=0;
bool not_empty;
char df_pwd[16];
char store_pwd[16];
char ent_pwd[16];
#define rst 50
#define del_f 49 
int kout=0;
//states
bool enrolled=false;
bool query_pwd=false;
bool query_finger=false;
bool reset=false; 
bool check=true;
bool query=false;
bool achk=false;
bool finger_enroll=false;
bool set_pwd=false;
//outputs
int i,j=0;;
#define pwd 22
#define fng 24
#define conf 26
#define enter 28
#define permit 30

#define power 34
#define failed 36
#define success 38

void setup() {
  // put your setup code here, to run once:
  lcd.begin(16,2);
  pinMode(power,OUTPUT);
  pinMode(failed,OUTPUT);
  pinMode(success,OUTPUT);
  pinMode(rst, INPUT);
  pinMode(del_f, INPUT);
  pinMode(pwd, OUTPUT);pinMode(fng, OUTPUT);pinMode(conf,OUTPUT);pinMode(enter, OUTPUT);pinMode(permit,OUTPUT);
  digitalWrite(pwd, LOW);digitalWrite(fng, LOW),digitalWrite(conf,LOW);digitalWrite(enter,LOW);digitalWrite(permit,LOW);
  Serial.begin(9600);
  while(!Serial);
  finger.begin(57600);
  if(finger.verifyPassword()){
    //Serial.println("fingerprint sensor found");
    digitalWrite(power,HIGH);
  }
  else{
    //Serial.println("fingerprint sensor not connected");
    delay(1);
  }
  if(EEPROM.read(0)==(0))not_empty=false;
  else not_empty=true;
  if(not_empty==false)first_time();
  else if(not_empty==true)set_password();
  set_password();
}
uint8_t readnumber(void) {
  uint8_t num = 0;  
  while (num == 0) {
    while (! Serial.available());
    num = Serial.parseInt();
  }
  return num;
}

void loop() {
  char key=customKeypad.getKey();
  outwrite("pwd",0);outwrite("fng",0);outwrite("conf",0);outwrite("enter",0);
  if((reset==false) and (finger_enroll==false)){
    lcd.setCursor(0,0);
    lcd.print("enter password"); 
    digitalWrite(pwd, LOW);digitalWrite(fng, LOW),digitalWrite(conf,LOW);digitalWrite(enter,LOW);digitalWrite(permit,LOW); 
  }
  if(digitalRead(rst)==HIGH){
    reset=true;
    enrolled=false;
    i=0;
    outwrite("enter",1);
    delay(1000);
    outwrite("enter",0);
    //Serial.println("enter old password:");
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("old password");
  }else if(key){ 
    if(reset==true){
      enrolled=false;
      query_pwd=false;
      set_pwd=false;
      finger_enroll=false;
      //face_enroll=false;
      check=false;
      query=false;
      achk=false;
      if((key=='#') or (i==15)){
        i=0;
        query_pwd=true;
      }else{
        lcd.setCursor(i,1);
        ent_pwd[i]=key;
        //Serial.print(key);
        lcd.print(key);
        i++;
      }
    } 
    if(query_pwd==true){
      if(strcmp(df_pwd,ent_pwd)==0){
        outwrite("conf",1);outwrite("pwd",1);
        delay(2000);
        outwrite("pwd",0);outwrite("conf",0);
        reset=false;
        set_pwd=true;
        memset(df_pwd,0,sizeof(df_pwd));
        //Serial.println("set new password:");
        lcd.clear();lcd.setCursor(0,0);lcd.print("new password");
        digitalWrite(failed,LOW);digitalWrite(success,HIGH);delay(1000);digitalWrite(success,LOW);
        memset(ent_pwd,0,sizeof(ent_pwd));
        key='A';
      }else{
        reset=true;
        outwrite("conf",0);outwrite("pwd",1);
        delay(1000);
        outwrite("pwd",0);outwrite("conf",0);
        //Serial.println("wrong password enter old password:");
        digitalWrite(failed,HIGH);
        lcd.clear();
        lcd.setCursor(0,0);lcd.print("old password:");
      }   
    } 
    if(set_pwd==true){
      query_pwd=false;
      if((key=='#') or (i==15)){
        key=' ';
        finger_enroll=true;
        set_password();
        i=0;
        j=0;
        memset(ent_pwd,0,sizeof(ent_pwd));
        //Serial.println("new password is");
        //Serial.println(df_pwd);
        lcd.clear();lcd.print("finger reg");
        key=' ';
      }else{
        lcd.setCursor(j,1);
        EEPROM.write(j,key);
        //Serial.print(key);
        lcd.print(key);
        i++;
        j++;
      }
    }
    if(finger_enroll==true){
      set_pwd=false;
      while(key==' '){key=customKeypad.getKey();}
      id=key;
      if(id==0){
        return;  
      }
      if(digitalRead(del_f)==HIGH){
        fingerprintdelete(id);
      }
      else if(digitalRead(del_f)==LOW){
        //Serial.print("Enrolling finger ");
        //Serial.print(id);
        while(!fingerprintenroll()){
          if(fingerprintenroll())break;  
        }
      }
      enrolled=true;
    }else{};
    if(enrolled==true){
      check=true;
      finger_enroll=false;
      outwrite("enter",1);
      delay(1000);
      outwrite("enter",0);
      key='A';
    }
    if(check==true){
      enrolled=false;
      if((key=='#') or (kout==15)){
        kout=0;
        reset=false;
        query_pwd=false;
        set_pwd=false;
        finger_enroll=false;
        achk=true;
        query=true;
      }else{
        lcd.setCursor(kout,1);
        query_pwd=false;
        ent_pwd[kout]=key;
        lcd.print(key);
        //Serial.print(key);
        kout++;
      } 
    }
  }
  if(achk==true){
    set_password();
    if(query==true){
      //Serial.println();
      if(strcmp(df_pwd, ent_pwd)==0){
        digitalWrite(failed,LOW);digitalWrite(success,HIGH);delay(1000);digitalWrite(success,LOW);
        outwrite("conf",1);outwrite("pwd",1);
        delay(2000);
        outwrite("pwd",0);outwrite("conf",0);
        checkfingerprint(); 
        query_finger=false;
        memset(ent_pwd, 0,sizeof(ent_pwd)); 
        //code to read fingerprint
      }else{
        digitalWrite(failed,HIGH);
        outwrite("conf",0);outwrite("pwd",1);
        delay(2000);
        outwrite("pwd",0);outwrite("conf",0);
        outwrite("enter",1);
        delay(1000);
        outwrite("enter",0);
        //Serial.print("wrong password");
        memset(ent_pwd, 0,sizeof(ent_pwd));
        lcd.clear();
        kout=0;
      }
    }
  }
  achk=false;
}

int checkfingerprint(){
  lcd.clear();lcd.setCursor(0,0);lcd.print("place finger");
  //Serial.print("place finger");
  int p=-1;
  while(p!=FINGERPRINT_OK){
    p=finger.getImage();
    switch(p){
      case FINGERPRINT_OK:
        //Serial.println("fingerprint is being read");
        break; 
      case FINGERPRINT_IMAGEFAIL: 
        //Serial.println("please replace finger");
        break;
    }
    p=finger.image2Tz();
    while(p!=FINGERPRINT_OK){
      switch(p){
        case FINGERPRINT_OK:
          //Serial.println("fingerprint read complete");
          break;
        case FINGERPRINT_IMAGEMESS:
          //Serial.println("fingerprint not clear, clean finger and wipe surface of fingerprint device");
          break;
      }  
    }
    p=finger.fingerFastSearch();
    if(p==FINGERPRINT_OK){digitalWrite(failed,LOW);digitalWrite(success,HIGH);
      outwrite("conf",1);outwrite("permit",1);
      delay(1000);
      outwrite("permit",0);outwrite("conf",0);
      digitalWrite(success,LOW);
      lcd.setCursor(0,1);lcd.print("access granted");
      //Serial.println("access granted");
      delay(2500);
      lcd.clear();
    }
    else if(p==FINGERPRINT_NOTFOUND){
      digitalWrite(failed,HIGH);
      outwrite("conf",0);outwrite("permit",1);
      delay(1000);
      outwrite("permit",0);outwrite("conf",0);
     //Serial.println("fingerprint not found, replace finger, make sure to wipe finger and fingerprint device surface");
     lcd.setCursor(0,1);lcd.print("access denied");
     checkfingerprint();
     return p;   
    }
  }  
}

uint8_t fingerprintenroll() {
  lcd.setCursor(0,0);lcd.print("enroll finger");
  outwrite("fng",0);
  int p = -1;
  while (p != FINGERPRINT_OK) {
    p = finger.getImage();
    switch (p) {
    case FINGERPRINT_OK:
      //Serial.println("Image taken");
      break;
    case FINGERPRINT_NOFINGER:
      //Serial.println(".");
      break;
    case FINGERPRINT_PACKETRECIEVEERR:
      //Serial.println("Communication error");
      break;
    case FINGERPRINT_IMAGEFAIL:
      //Serial.println("Imaging error");
      break;
    default:
      //Serial.println("Unknown error");
      break;
    }
  }

  // OK success!

  p = finger.image2Tz(1);
  switch (p) {
    case FINGERPRINT_OK:
      //Serial.println("Image converted");
      break;
    case FINGERPRINT_IMAGEMESS:
      //Serial.println("Image too messy");
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      //Serial.println("Communication error");
      return p;
    case FINGERPRINT_FEATUREFAIL:
      //Serial.println("Could not find fingerprint features");
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      //Serial.println("Could not find fingerprint features");
      return p;
    default:
      //Serial.println("Unknown error");
      return p;
  }

  delay(2000);
  p = 0;
  while (p != FINGERPRINT_NOFINGER) {
    p = finger.getImage();
  }
  //Serial.print("ID "); Serial.println(id);
  p = -1;
  //Serial.println("Place same finger again");
  lcd.setCursor(0,0);lcd.print("reenroll finger");
  while (p != FINGERPRINT_OK) {
    p = finger.getImage();
    switch (p) {
    case FINGERPRINT_OK:
      //Serial.println("Image taken");
      break;
    case FINGERPRINT_NOFINGER:
      //Serial.print(".");
      break;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Communication error");
      break;
    case FINGERPRINT_IMAGEFAIL:
      //Serial.println("Imaging error");
      break;
    default:
      //Serial.println("Unknown error");
      break;
    }
  }

  // OK success!

  p = finger.image2Tz(2);
  switch (p) {
    case FINGERPRINT_OK:
      //Serial.println("Image converted");
      break;
    case FINGERPRINT_IMAGEMESS:
      //Serial.println("Image too messy");
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      //Serial.println("Communication error");
      return p;
    case FINGERPRINT_FEATUREFAIL:
      //Serial.println("Could not find fingerprint features");
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      //Serial.println("Could not find fingerprint features");
      return p;
    default:
      //Serial.println("Unknown error");
      return p;
  }
  
  // OK converted!
  //Serial.print("Creating model for #");  Serial.println(id);
  
  p = finger.createModel();
  if (p == FINGERPRINT_OK) {
    //Serial.println("Prints matched!");
    outwrite("conf",1);outwrite("fng",1);
    delay(2000);
    outwrite("fng",0);outwrite("conf",0);
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    //Serial.println("Communication error");
    return p;
  } else if (p == FINGERPRINT_ENROLLMISMATCH) {
    //Serial.println("Fingerprints did not match");
    digitalWrite(failed,HIGH);
    lcd.setCursor(0,1);lcd.print("failure");
    outwrite("conf",0);outwrite("fng",1);
    delay(1000);
    outwrite("fng",0);outwrite("conf",0);
    lcd.clear();
    return p;
  } else {
    Serial.println("Unknown error");
    return p;
  }   
  
  Serial.print("ID "); Serial.println(id);
  p = finger.storeModel(id);
  if (p == FINGERPRINT_OK) {
    //Serial.println("Stored!");digitalWrite(failed,LOW);
    digitalWrite(success,HIGH);
    lcd.setCursor(0,1);lcd.print("enrolled");
    delay(1500);
    lcd.clear();
    digitalWrite(success,LOW);
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    //Serial.println("Communication error");
    outwrite("conf",0);outwrite("fng",1);
    delay(1000);
    outwrite("fng",0);outwrite("conf",0);
    return p;
  } else if (p == FINGERPRINT_BADLOCATION) {
    //Serial.println("Could not store in that location");
    outwrite("conf",0);outwrite("fng",1);
    delay(1000);
    outwrite("fng",0);outwrite("conf",0);
    return p;
  } else if (p == FINGERPRINT_FLASHERR) {
    //Serial.println("Error writing to flash");
    outwrite("fng",1);outwrite("conf",0);
    delay(1000);
    outwrite("conf",0);outwrite("fng",0);
    return p;
  } else {
    //Serial.println("Unknown error");
    outwrite("conf",0);outwrite("fng",1);
    delay(1000);
    outwrite("fng",0);outwrite("conf",0);
    return p;
  }   
}

uint8_t fingerprintdelete(uint8_t id) {
  uint8_t p = -1;
  lcd.clear();lcd.setCursor(0,0);lcd.print("delete finger");
  p = finger.deleteModel(id);

  if (p == FINGERPRINT_OK) {
    digitalWrite(failed,LOW);digitalWrite(success,HIGH);delay(1000);digitalWrite(success,LOW);
    outwrite("conf",1);outwrite("fng",1);
    delay(2000);
    outwrite("fng",0);outwrite("conf",1);
    //Serial.println("Deleted!");
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
        //Serial.println("Communication error");
    return p;
  } else if (p == FINGERPRINT_BADLOCATION) {
    //Serial.println("Could not delete in that location");
    return p;
  } else if (p == FINGERPRINT_FLASHERR) {
    //Serial.println("Error writing to flash");
    return p;
  } else {
    //Serial.print("Unknown error: 0x"); Serial.println(p, HEX);
    return p;
  }   
}

void first_time(){
  String dft_pwd="1234567";
  unsigned int _size=dft_pwd.length();
  i=0;
  while(dft_pwd[i]!='\0'){
    EEPROM.write(address+i,dft_pwd[i]);
    i++;  
  }
  EEPROM.write(address+_size,'\0');
  i=0;
}

void set_password(){
  i=0;
  while(EEPROM.read(address+i)!='\0'){
    df_pwd[i]=EEPROM.read(address+i);
    i++;
  }
  //df_pwd[i++]='\0';
}

void clear_eeprom(){ 
  for (int i = 0 ; i < EEPROM.length() ; i++) {
    EEPROM.write(i, 0);
  }
}
void outwrite(String out,int val){
  int in;
  if(out=="pwd")in=22;
  if(out=="fng")in=24;
  if(out=="conf")in=26;
  if(out=="enter")in=28;
  if(out=="permit")in=30;
  if(val==1)digitalWrite(in,HIGH);
  else if(val==0)digitalWrite(in,LOW);  
}
