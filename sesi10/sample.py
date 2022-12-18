import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
MataKuliah = ['Matematika', 'Fisika', 'Kimia', 'Komputer', 'Bahasa']
Nilai = [80,90,65,79,82]
ax.pie(Nilai,labels=MataKuliah,autopct='%1.2f%%')
plt.show()