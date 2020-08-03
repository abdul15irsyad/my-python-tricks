# mendeklarasikan banyak variabel sekaligus
nama1, umur1 = 'irsyad',21
print('nama saya', nama1 + ', saya', umur1 ,'tahun')

# varibale nama2 memiliki nilai yang pertama, sedangkan *hobby adalah nilai sisanya
nama2, *hobby2 = 'abdul','coding','photoshop','basket'
print('nama saya', nama2 + ', saya menyukai', ', '.join(hobby2))

# mendeklarasikan beberapa variabel yang memiliki nilai sama
x = y = z = 15
print('x =',x,'\ny =',y,'\nz =',z)