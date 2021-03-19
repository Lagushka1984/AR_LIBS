class Motion():
    def __init__(self, mt_file):
        self.mt_file = mt_file
        self.RestFile()
        self.pages = []
        self.GetPage()

    def GetDXL(self):
        drow = ""
        for row in mt_file:
            if row.find("enable=0") != -1 or row.find("enable=1") != -1:
                drow = row[7:]
                break
        ids = []
        for col in drow:
            if col == "0" or col == "1":
                ids.append(int(col))
        idds = []
        for i in range(0, len(ids)):
            if ids[i] == 1:
                idds.append(i)
        return idds

    def RestFile(self):
        x = 0
        for i in range(0, len(self.mt_file)):
            if self.mt_file[i] == "page_begin\n":
                self.mt_file[i] = str(x)
                x += 1

    def GetPage(self):
        trig = False
        word = []
        for row in self.mt_file:
            if row == "page_end\n":
                trig = False
                self.pages.append(word)
                word = []
            if trig:
                word.append(row)
            if row.isdigit() == True:
                trig = True
            
    def GetStep(self, pp):
        step = []
        for page in pp:
            if page.startswith("step"):
                step.append(page[5:])
        return step

    def GetMotion(self, num):
        motion = []
        page = self.pages[num - 1]
        step = self.GetStep(page)
        for s in step:
            ss = []
            word = ""
            for i in s:
                try:
                    if i != ".":
                        int(i)
                    word += i
                except:
                    ss.append(word)
                    word = ""
            ss2 = []
            for i in ss:
                ss2.append(float(i))
            motion.append(ss2)
        return motion

class PlayMotion(Motion):
    def __init__(self, num):
        self.dxl_list = self.GetDXL
        self.dxl = []
        self.motion = self.GetMotion(num)
    
    def PlayAX(self):
        for i in list_dxl:
            self.dxl.append(AX(i))


#mt_file = open("mmm.txt", "r").readlines()
#motion = Motion(mt_file)
#ids = motion.GetDXL()
#print(ids)
#print(motion.pages[245])
#print(motion.mt_file)
#print(motion.GetMotion(2))
