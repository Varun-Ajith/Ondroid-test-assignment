const uint8_t l = 10;
uint8_t pins[l] = {
27,//1
25,//2
33,//3
21,//4
26,//5
23,//6
22,//7
12,//8
19,//9
13 //10
};

void setup(){
    for (int i=0; i<l; i++){
        pinMode(pins[i], OUTPUT);
    }
}
void loop() {
    for(int i=0;i<l+1; i++){
        if (i>0){
            digitalWrite(pins[i-1], LOW);
        }
        if (i<l){
            digitalWrite(pins[i], HIGH);
        }
        delay(200);
    } 
}
