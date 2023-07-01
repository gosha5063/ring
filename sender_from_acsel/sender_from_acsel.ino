#include "I2Cdev.h"                  // Подключение библиотеки I2Cdev
#include "MPU6050.h"                 // Подключение библиотеки MPU6050 
#include "Wire.h"                    // Подключение библиотеки WireCdev
MPU6050 CY531;                       // Создаем объект, символизирующий модуль датчика
int16_t ax, ay, az;                  // Переменные для хранения значений акселерометра
int16_t gx, gy, gz;   
float calix = -1;    
float caliy = -1;            // Переменные для хранения значений гироскоп
void setup()
{
Serial1.begin(9600);
Wire.begin();                         // Инициализация Wire
Serial.begin(9600);                  // Инициализация последовательного порта
Serial.println("Initializing I2C devices..."); // Печать текста
CY531.initialize();                   // Инициализация MPU
delay(100);                           // Пауза
}
void loop()
{
CY531.getMotion6(&ax, &ay, &az, &gx, &gy, &gz); // Чтение значений гироскопа и акселерометра
float ay_res = (((float)ay/16300)+1)/2;
ay_res = max(0, min(1, ay_res));
int new_y = ay_res*271;
new_y = new_y/16;
Serial1.write(new_y);
delay(100);
}