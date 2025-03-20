from datetime import datetime

class Sorozatok:
    def __init__(self, sor):
        reszek = sor
        if reszek[0] == "NI":
            self.adas = reszek[0]
        else:    
            self.adas = datetime.strptime(reszek[0], '%Y.%m.%d').date()
        self.cim = reszek[1]
        self.evad_resz = reszek[2]
        self.hosszusag = int(reszek[3])
        self.latta_e = reszek[4]
    def __str__(self):
        return f"{self.adas} {self.cim} {self.evad_resz} {self.hosszusag} {self.latta_e}"

f = open('lista-1.txt', encoding='utf-8')

sorozatok_obj = []

def beolvas(file):
    lines = f.readlines()
    data = [line.strip() for line in lines]
    groupped_data = [data[i:i+5] for i in range(0, len(data), 5)]
    for item in groupped_data:
        sorozatok_obj.append(Sorozatok(item))

def date_count():
    dateCount = 0
    for item in sorozatok_obj:
        if item.adas != "NI":
            dateCount += 1
    print(f"2. feladat \n   A listában {dateCount} db vetítési dátummal rendelkező epizód van. ")


def seen_precent():
    seen = 0
    notseen = 0
    for item in sorozatok_obj:
        if item.latta_e == "0":
            notseen += 1
        else:
            seen += 1
    print(f"3. feladat \n    A listában lévő epizódok {round(seen/len(sorozatok_obj)*100, 2)}%-át látta.")

def spent_time():
    time_in_minutes = 0
    for item in sorozatok_obj:
        if item.latta_e == "1":
            time_in_minutes += item.hosszusag
    days = time_in_minutes // (24 * 60)
    remaining_minutes = time_in_minutes % (24 * 60)
    hours = remaining_minutes // 60
    minutes = remaining_minutes % 60

    print(f"4. feladat \n   Sorozatnézéssel {days} napot {hours} órát és {minutes} percet töltött. ")

def date_unseen():
    print("5.feladat")
    date = input("  Adjon meg egy dátumot!")
    date_obj = datetime.strptime(date, '%Y.%m.%d').date()
    for item in sorozatok_obj:
            try: 
                if item.adas <= date_obj and item.latta_e == "0":
                    print(f"{item.evad_resz}    {item.cim}")
            except TypeError: 
                pass



def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]     
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev = ev - 1
    het_napja = napok[(ev + ev // 4 - ev // 100 + ev % 400 + honapok[ho-1] + nap) % 7]
    return het_napja

def nap_adas():
    nap_lista = []
    nap_heten = input("Adja meg a hét egy napját (például cs)! ")
    for item in sorozatok_obj:
        try:
            temp = hetnapja(item.adas.year, item.adas.month, item.adas.day)
            if temp == nap_heten:
                if item.cim not in nap_lista:
                    nap_lista.append(item.cim)
        except AttributeError:
            pass
    for i in range(len(nap_lista)):
        print(nap_lista[i])

f2 = open('summa.txt', "a")

def write_to_file():
    row_list = [] 
    titles = []

    for i in sorozatok_obj:
        if i.cim not in titles:
            titles.append(i.cim)
    for i in titles:
        titles_i = i
        ep_count = 0
        time_count = 0
        for item in sorozatok_obj:
            if i == item.cim:
                ep_count += 1
                time_count += item.hosszusag
        row_list = [titles_i, time_count, ep_count]
        f2.write(f"{row_list[0]} {row_list[1]} {row_list[2]}\n")
    


def main():
    beolvas(f)
    date_count()
    seen_precent()
    spent_time()
    date_unseen()
    nap_adas()
    write_to_file()
main()