class studentRecord:
    def __init__(self,i,Name):
        self.studentId=i
        self.studentName=Name

    def get_student_id(self):
        return self.studentId
    
    def set_student_id(self,i):
        self.studentId=i
        
    def __str__(self):
        return str(self.studentId) + " " + self.studentName


class HashTable:
    def __init__(self,tableSize=11):
        self.m=tableSize
        self.array=[None]*self.m
        self.n=0 #number of records

    def hash1(self,key):
        return(key%self.m)

    def insert(self,newRecord):
        key=newRecord.get_student_id()
        h=self.hash1(key)
        location=h
        for i in range(1,self.m):
            if self.array[location] is None or self.array[location].get_student_id()==-1:
                self.array[location]=newRecord
                self.n+=1
                return
            if self.array[location].get_student_id()==key:
                raise InvalidOperationException("Dublicate key")
            location=(h+i)%self.m
        print("the table is full")

    def search(self,key):
        h=self.hash1(key)
        location=h
        for i in range(1,self.m):
            if self.array[location]is None:
                return None
            if self.array[location].get_student_id()==key:
                return self.array[location]
            location=(h+1)%self.m
        return None


    def display(self):
        for i in range(self.m):
            print("[",end=" ");print(i,end=" ");print("]",end=" ")
            if self.array[i] is not None and self.array[i].get_student_id()!=-1:
                print(self.array[i])
            else:print("____")
            
    def delete(self,key):
        h=self.hash1(key)
        location=h
        for i in range(1,self.m):
            if self.array[location]is None:
                return None
            if self.array[location].get_student_id()==key:
                temp=self.array[location]
                self.array[location].set_student_id(-1)
                self.n-=1
                return temp
            location=(h+i)%self.m

        return None
######################################################
size=int(input("Enter initial size of table:"))
table=HashTable(size)
while True:
    print("1.Insert a record")
    print("2.Search a record")
    print("3.Delete a record")
    print("4.Display a record")
    print("5.Exist")
    option=int(input("enter your option:"))
    if option==1:
        id=int(input("enter the student id: "))
        name=input("enter the student Name: ")
        aRecord=studentRecord(id,name)
        table.insert(aRecord)
    elif option==2:
        id=int(input("enter the search id: "))
        aRecord=table.search(id)
        if aRecord is None:
            print("key not found")
        else:
            print(aRecord)
    elif option==3:
        id=int(input("enter the delete key"))
        table.delete(id)
    elif option==4:
        table.display()
    elif option==5:
        break
    else:print("wrong option")
    print()
        
        
    
    
                
        
        
