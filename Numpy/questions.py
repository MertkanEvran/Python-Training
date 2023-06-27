import numpy as np
# 1-) (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
np_array = np.array((10,15,30,45,60))
print(np_array)
# 2-) 5 - 15 arasındaki sayılarla numpy dizisi oluşturunuz.
np_array2 = np.arange(5,15)
print(np_array2)
# 3-) 50 - 100 arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
np_array3 = np.arange(50,100,5)
print(np_array3)
# 4-) 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
np_array4 = np.zeros(10)
print(np_array4)
# 5-) 10 elemanlı birlerden oluşan bir dizi oluşturunuz.
np_array5 = np.ones(10)
print(np_array5)
# 6-) (0-100) arasındaki eşit aralıklı 5 sayı üretin.
np_array6 = np.linspace(0,100,5)
print(np_array6)
# 7-) (10-30) arasında rastgele 5 tane tamsayı üretin.
np_array7 = np.random.randint(10,30,5)
print(np_array7)
# 8-) [-1 ile 1] arasında 10 sayı üretiniz.
np_array8 = np.random.randn(10)
print(np_array8)
# 9-) (3x5) boyutlarında  (10-50) arasında rastgele bir matris oluşturunuz.
np_array9 = np.random.randint(10,50,15)
multinp_array9 = np_array9.reshape(3,5)
print(multinp_array9)
# 10-) Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız.
print(multinp_array9.sum(axis=1))
print(multinp_array9.sum(axis=0))
# 11-) Üretilen matrisin en büyük, en küçük ve ortalama değerleri nedir.
print(f"Ortalama: {multinp_array9.mean()}")
print(f"Maksimum: { multinp_array9.max()}")
print(f"Minimum: {multinp_array9.min()}")
# 12-) Üretilen matrisin en büyük değerinin indeksi kaçtır.
print(multinp_array9.argmax())
# 13-) (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanın seçiniz.
np_array10 = np.arange(10,20)
print(np_array10[0:3])
# 14-) Üretilen dizinin elemanlarını terstten yazdırınız.
print(np_array10[::-1])
# 15-) Üretilen matrisin ilk satırını seçiniz
print(multinp_array9[0])
# 16-) Üretilen matrisin 2. satır 3. sütunundaki değer nedir.
print(multinp_array9[2,3])
# 17-) Üretilen matrisin tüm satırlardaki ilk elemanı nedir.
print(multinp_array9[:,0])
# 18-) Üretilen matrisin her bir elemanının karesini alınız.
print(multinp_array9 ** 2)
# 19-) Üretilen matris elemanlarının hangisi pozitif çift sayıdır.
np_matris = np.random.randint(-50,50,9).reshape(3,3)
pozitif = np_matris > 0
result = pozitif % 2 == 0
print(result)
