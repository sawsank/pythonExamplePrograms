##Using shutil module

from shutil import copyfile
copyfile("/root/a.txt","/root/b.txt")

"""Method	Preserves Permissions	Supports Directory as Destination	Copies Metadata	Supports file object
copy()	        Yes                 	Yes     No	                                    No
copyfile()	    No	                    No	    No	                                    No
copy2()	        Yes	                    Yes	    Yes	                                    No
copyfileobj()	No	                    No	     No	                                    Yes                     """