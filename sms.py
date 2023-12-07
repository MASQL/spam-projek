@@ -10,39 +10,28 @@ def menu(self):
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;       S P A M  S M S      ;
		;---------------------------;
		; Author : Bayu_Julianto    ;
		; Contact : t.me/kang_nuubi ;
		;       Author : MASQL      ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
1. Spam TRI
2. Spam HooqTV
3. Spam HooqTv (GUI)
4. Spam TelkomNyet
5. Spam Sms Gratis
6. Spam Sms Gratis (GUI)
7. Sms Gratis PayuTerus
8. Sms Gratis PayuTerus (GUI)
9. ALTBalaji OTP Spammer
NOTE: This tool's only work for Indonesia number phone.
1. SMS Gratis
2. OTP Matahari
3. OTP Hallodok
4. OTP Olx.co.id
5. OTP Sociolla.com
""")
		pilih=int(input('/Kang-newbie: '))
		pilih=int(input('noobie/> '))
		if pilih == 1:
			import src.sms
			import src.payu
		elif pilih == 2:
			import src.hooq
			import src.matahari
		elif pilih == 3:
			import src.hooqgui
			import src.alodok
		elif pilih == 4:
			import src.telnyet2
			import src.olx
		elif pilih == 5:
			import src.gratis
		elif pilih == 6:
			import src.gratisgui
		elif pilih == 7:
			import src.payu
		elif pilih == 8:
			import src.payugui
		elif pilih == 9:
			import src.balaji
			import src.socil
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
            #remove cache
                    try:
                        shutil.rmtree("src/__pycache__")
                    except: pass
                    if os.name in ['nt','win32']:
                        os.system('cls')
                    else: os.system('clear')
                    self.menu()
            try:
                Main()
            except KeyboardInterrupt:
                exit('[Exit] Key interrupt')
            except Exception as F:
                print('Err: %s'%(F))