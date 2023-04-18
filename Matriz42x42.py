terrenos = {
    "grama": 10,
    "areia": 20,
    "floresta": 100,
    "montanha": 150,
    "agua": 180,
}

Matriz = [
    #Linha 0
    [
        "floresta", "floresta", "floresta", "floresta", "floresta", "floresta",
	    "floresta", "floresta", "floresta", "floresta", "floresta", "floresta",
	    "floresta", "floresta", "floresta", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
	],

    #Linha 1
    [
        "floresta", "grama", "grama", "floresta", "grama", "floresta",
		"grama", "floresta", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "areia", "areia",
		"areia", "areia", "areia", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "areia", "areia", "areia",
		"areia", "montanha", "montanha", "montanha", "montanha", "montanha",
	],

    #Linha 2
    [
        "floresta", "grama", "grama", "floresta", "grama", "grama",
		"grama", "floresta", "grama", "floresta", "grama", "grama",
		"grama", "grama", "grama", "grama", "montanha", "montanha",
		"montanha", "montanha", "montanha", "areia", "areia", "areia",
		"areia", "areia", "areia", "areia", "montanha", "montanha",
		"montanha", "montanha", "areia", "areia", "areia", "areia",
		"areia", "areia", "montanha", "montanha", "montanha", "montanha",
	],

    #Linha 3
    [
        "floresta", "grama", "floresta", "floresta", "grama", "floresta",
		"grama", "floresta", "grama", "floresta", "grama", "grama",
		"floresta", "grama", "grama", "grama", "grama", "montanha",
		"areia", "areia", "areia", "areia", "areia", "areia",
		"areia", "areia", "areia", "areia", "areia", "areia",
		"areia", "areia", "areia", "areia", "areia", "areia",
		"areia", "areia", "areia", "areia", "montanha", "montanha",
	],

    #Linha 4
    [
        "floresta", "grama", "grama", "grama", "grama", "floresta",
		"grama", "floresta", "grama", "floresta", "grama", "grama",
		"floresta", "grama", "grama", "grama", "grama", "montanha",
		"areia", "montanha", "montanha", "areia", "areia", "areia",
		"areia", "areia", "areia", "areia", "montanha", "montanha",
		"montanha", "montanha", "areia", "areia", "areia", "areia",
		"areia", "areia", "montanha", "montanha", "montanha", "montanha",
	],

    #Linha 5
    [
        "floresta", "grama", "floresta", "floresta", "grama", "floresta",
		"grama", "floresta", "grama", "floresta", "grama", "floresta",
		"floresta", "floresta", "grama", "grama", "grama", "montanha",
		"areia", "montanha", "montanha", "montanha", "areia", "areia",
		"areia", "areia", "areia", "montanha", "montanha", "montanha",
		"montanha", "agua", "montanha", "areia", "areia", "areia",
		"areia", "montanha", "agua", "montanha", "montanha", "montanha",
    ],

    #Linha 6
    [
        "floresta", "grama", "floresta", "floresta", "grama", "floresta",
		"grama", "grama", "grama", "floresta", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "montanha",
		"areia", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "agua", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "agua", "montanha", "montanha", "montanha",
    ],

    #Linha 7
    [
        "floresta", "grama", "floresta", "floresta", "floresta", "floresta",
		"grama", "floresta", "floresta", "floresta", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "montanha",
		"areia", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "agua", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "agua", "montanha", "grama", "montanha",
	],

    #Linha 8
    [
        "floresta", "grama", "grama", "floresta", "grama", "grama",
		"grama", "grama", "grama", "floresta", "grama", "grama",
		"agua", "grama", "grama", "grama", "grama", "montanha",
		"areia", "areia", "areia", "areia", "areia", "areia",
		"areia", "areia", "areia", "areia", "areia", "montanha",
		"montanha", "agua", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "agua", "montanha", "grama", "montanha",
    ],

    #Linha 9
    [
        "floresta", "floresta", "floresta", "floresta", "grama", "floresta",
		"floresta", "floresta", "grama", "grama", "grama", "agua",
		"agua", "agua", "grama", "grama", "grama", "montanha",
		"areia", "montanha", "montanha", "montanha", "montanha", "montanha",
		"areia", "montanha", "montanha", "montanha", "areia", "montanha",
		"montanha", "agua", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "agua", "montanha", "grama", "montanha",
	],

    [		
		"floresta", "floresta", "floresta", "floresta", "grama", "floresta", 
		"floresta", "floresta", "grama", "grama", "grama", "agua",
		"agua", "agua", "grama", "grama", "grama", "montanha", 
		"areia", "montanha", "montanha", "montanha", "montanha", "montanha",  
		"areia", "montanha", "montanha", "montanha", "areia", "montanha", 
		"montanha", "agua", "montanha", "montanha", "montanha", "montanha", 
		"montanha", "montanha", "agua", "montanha", "grama", "montanha",
	],



    [		
		"floresta", "grama", "grama", "floresta", "grama", "grama",  
		"grama", "grama", "grama", "grama", "agua", "agua",
		"agua", "agua", "agua", "grama", "grama", "montanha", 
		"montanha", "montanha", "floresta", "floresta", "floresta", "montanha",  
		"montanha", "montanha", "floresta", "floresta", "floresta", "floresta",
		"floresta", "agua", "grama", "grama", "montanha", "montanha", 
		"grama", "grama", "agua", "grama", "grama", "montanha",
	],


    [		
		"floresta", "grama", "grama", "floresta", "grama", "grama",  
		"floresta", "grama", "grama", "grama", "grama", "agua",
		"agua", "agua", "grama", "grama", "grama", "grama", 
		"grama", "grama", "grama", "grama", "grama", "grama",   
		"grama", "grama", "grama", "grama", "grama", "grama", 
		"agua", "agua", "agua", "agua", "agua", "agua",
		"agua", "agua", "agua", "grama", "grama", "montanha",
	],


    [		
		"floresta", "grama", "grama", "floresta", "grama", "grama",  
		"floresta", "grama", "grama", "grama", "grama", "grama",
		"agua", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "grama",   
		"grama", "grama", "grama", "grama", "grama", "grama", 
		"agua", "grama", "grama", "floresta", "grama", "grama", 
		"grama", "grama", "grama", "floresta", "grama", "montanha",
	],


    [		
		"floresta", "grama", "grama", "floresta", "grama", "grama",  
		"floresta", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "floresta", 
		"floresta", "floresta", "grama", "grama", "grama", "floresta", 
		"floresta", "floresta", "floresta", "grama", "grama", "grama", 
		"agua", "grama", "grama", "grama", "grama", "grama", 
		"grama", "floresta", "grama", "floresta", "grama", "montanha",
	],


    [		
		"floresta", "grama", "grama", "grama", "grama", "grama", 
		"grama", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "grama", 
		"agua", "grama", "floresta", "grama", "floresta", "grama", 
		"floresta", "floresta", "grama", "floresta", "grama", "montanha",
	],


    [		
		"floresta", "grama", "floresta", "floresta", "floresta", "floresta", 
		"floresta", "grama", "floresta", "floresta", "floresta", "grama",
		"grama", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "grama", 
		"agua", "grama", "grama", "grama", "grama", "grama",  
		"grama", "grama", "grama", "grama", "grama", "montanha",
	],


    [		
		"floresta", "grama", "grama", "grama", "grama", "grama", 
		"grama", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "agua",
		"agua", "agua", "agua", "agua", "agua", "agua", 
		"agua", "agua", "agua", "grama", "grama", "grama", 
		"grama", "grama", "montanha", "montanha", "montanha", "montanha", 
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
	],


    [		
		"floresta", "grama", "grama", "grama", "grama", "grama", 
		"grama", "grama", "grama", "agua", "grama", "grama",
		"floresta", "grama", "floresta", "grama", "grama", "agua",
		"grama", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "agua", "grama", "grama", "grama", 
		"agua", "grama", "montanha", "areia", "areia", "areia",
		"areia", "areia", "areia", "areia", "areia", "montanha",
	],



    [		
		"floresta", "grama", "floresta", "grama", "grama", "floresta",
		"grama", "grama", "grama", "agua", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "agua",
		"grama", "floresta", "grama", "grama", "grama", "grama",
		"floresta", "grama", "agua", "agua", "agua", "agua", 
		"agua", "grama", "montanha", "areia", "montanha", "areia",
		"areia", "montanha", "areia", "areia", "areia", "montanha",
	],


    [		
		"floresta", "grama", "floresta", "grama", "grama", "floresta",
		"grama", "grama", "grama", "agua", "grama", "grama",
		"floresta", "grama", "floresta", "grama", "grama", "grama",
		"grama", "floresta", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "grama",  "grama", "grama",
	 	"grama", "grama", "montanha", "areia", "montanha", "montanha", 
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
	],



    [		
		"floresta", "grama", "floresta", "grama", "grama", "floresta",
		"grama", "grama", "grama", "agua", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "agua",
		"grama", "grama", "grama", "agua", "grama", "grama",
		"grama", "grama", "agua", "grama",  "grama", "grama",
	 	"montanha", "grama", "montanha", "areia", "areia", "areia", 
		"areia", "areia", "areia", "areia", "areia", "montanha",
	],


    [		
		"floresta", "grama", "floresta", "grama", "grama", "floresta",
		"grama", "grama", "grama", "agua", "grama", "floresta", 
		"floresta", "floresta", "floresta", "grama", "grama", "agua",
		"grama", "floresta", "grama", "grama", "grama", "grama",
		"floresta", "grama", "grama", "grama",  "grama", "grama",
	 	"montanha", "grama", "montanha", "areia", "montanha", "montanha", 
		"montanha", "montanha", "areia", "montanha", "montanha", "montanha",
	],


    [		
		"floresta", "grama", "grama", "grama", "grama", "grama", 
		"grama", "grama", "grama", "agua", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "agua",
		"grama", "grama", "grama", "grama", "grama", "grama", 
		"grama", "grama", "agua", "grama", "montanha", "grama", 
		"montanha", "grama", "montanha", "areia", "areia", "areia", 
		"areia", "areia", "areia", "areia", "areia", "montanha",
	],


    [		
		"floresta", "grama", "grama", "grama", "grama", "grama", 
		"grama", "grama", "grama", "grama", "grama", "floresta",
		"floresta", "floresta", "floresta", "grama", "grama", "agua",
		"agua", "agua", "agua", "grama", "grama", "agua", 
		"agua", "agua", "agua", "grama", "montanha", "grama", 
		"montanha", "grama", "montanha", "montanha", "montanha", "areia", 
		"areia", "montanha", "montanha", "montanha", "montanha", "montanha",
	],


    [		
		"floresta", "floresta", "floresta", "floresta", "floresta", "floresta", 
		"floresta", "grama", "grama", "floresta", "floresta", "floresta",
		"floresta", "floresta", "floresta", "floresta", "floresta", "floresta",
		"grama", "grama", "grama", "grama", "grama", "grama", 
		"grama", "grama", "agua", "grama", "montanha", "grama", 
		"montanha", "grama", "grama", "grama", "grama", "grama", 
		"grama", "grama", "grama", "grama", "grama", "montanha",
	],


    [		
		"floresta", "floresta", "floresta", "floresta", "floresta", "floresta", 
		"grama", "grama", "floresta", "floresta", "floresta", "floresta",
		"floresta", "grama", "floresta", "floresta", "floresta", "floresta",
		"floresta", "grama", "floresta", "floresta", "floresta", "grama", 
		"grama", "grama", "agua", "grama", "montanha", "grama", 
		"grama", "grama", "grama", "grama", "grama", "grama", 
		"grama", "grama", "grama", "grama", "grama", "montanha",
	],


    [		
		"floresta", "grama", "floresta", "grama", "floresta", "grama",
		"grama", "grama", "floresta", "floresta", "floresta", "floresta",
		"grama", "grama", "grama", "floresta", "floresta", "floresta",
		"floresta", "grama", "floresta", "floresta", "floresta", "grama", 
		"grama", "grama", "agua", "grama", "montanha", "grama", 
		"grama", "grama", "montanha", "montanha", "montanha", "montanha", 
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
	],


    [		
		"montanha", "grama", "grama", "grama", "floresta", "grama",
		"grama", "grama", "floresta", "floresta", "floresta", "grama",
		"grama", "grama", "grama", "grama", "floresta", "floresta",
		"floresta", "grama", "grama", "grama", "grama", "grama", 
		"grama", "grama", "agua", "grama", "grama", "grama", 
		"grama", "grama", "grama", "grama", "grama", "montanha", 
		"grama", "grama", "grama", "grama", "grama", "montanha", 
	],


    [		
		"montanha", "grama", "grama", "grama", "floresta", "grama",
		"grama", "grama", "floresta", "floresta", "floresta", "floresta",
		"grama", "grama", "grama", "floresta", "floresta", "floresta",
		"floresta", "grama", "floresta", "grama", "grama", "grama", 
		"grama", "grama", "agua", "grama", "grama", "grama", 
		"grama", "grama", "grama", "grama", "grama", "montanha", 
		"grama", "grama", "grama", "grama", "grama", "montanha", 
	],


    [		
		"montanha", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "floresta", "floresta", "floresta",
		"floresta", "grama", "floresta", "floresta", "floresta", "floresta",
		"grama", "grama", "floresta", "grama", "grama", "grama", 
		"grama", "grama", "agua", "agua", "agua", "grama", 
		"agua", "agua", "agua", "agua", "grama", "montanha", 
		"grama", "montanha", "montanha", "montanha", "montanha", "montanha", 
	],


    [		
		"montanha", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "agua", "grama", "grama",
		"grama", "grama", "grama", "grama", "grama", "montanha",
	],


    [		
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "grama", "grama", "grama",
		"grama", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "grama", "grama", "montanha", "montanha",
		"montanha", "montanha", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "agua", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "grama", "montanha",
	],


    [		
		"montanha", "areia", "areia", "areia", "areia", "areia", 
		"areia", "areia", "montanha", "grama", "grama", "grama",
		"grama", "montanha", "grama", "grama", "grama", "grama", 
		"grama", "grama", "grama", "grama", "grama", "grama", 
		"grama", "montanha", "grama", "grama", "grama", "grama",
		"grama", "grama", "grama", "agua", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
	],


    [		
		"montanha", "areia", "montanha", "montanha", "areia", "areia", 
		"areia", "areia", "montanha", "grama", "grama", "grama",
		"grama", "montanha", "grama", "grama", "grama", "grama", 
		"grama", "grama", "grama", "grama", "floresta", "grama", 
		"grama", "montanha", "grama", "grama", "agua", "agua", 
		"agua", "agua", "agua", "agua", "agua", "agua", 
		"montanha", "montanha", "agua", "agua", "montanha", "montanha",
	],


    [		
		"montanha", "areia", "montanha", "montanha", "areia", "areia", 
		"areia", "areia", "montanha", "grama", "grama", "grama",
		"grama", "montanha", "grama", "floresta", "grama", "grama", 
		"agua", "agua", "grama", "grama", "floresta", "grama", 
		"grama", "montanha", "grama", "grama", "agua", "agua", 
		"montanha", "agua", "agua", "agua", "agua", "agua", 
		"montanha", "montanha", "agua", "agua", "montanha", "montanha",
	],


    [		
		"montanha", "areia", "areia", "areia", "areia", "areia", 
		"areia", "areia", "montanha", "grama", "grama", "montanha",
		"grama", "montanha", "grama", "grama", "grama", "grama", 
		"agua", "agua", "grama", "grama", "floresta", "grama", 
		"grama", "montanha", "grama", "grama", "agua", "agua", 
		"agua", "agua", "montanha", "montanha", "agua", "agua", 
		"montanha", "montanha", "agua", "agua", "montanha", "montanha",
	],


    [		
		"montanha", "areia", "areia", "areia", "areia", "areia", 
		"areia", "areia", "montanha", "grama", "grama", "montanha",
		"grama", "grama", "grama", "grama", "grama", "grama", 
		"grama", "grama", "grama", "grama", "grama", "grama", 
		"grama", "montanha", "grama", "grama", "agua", "agua", 
		"agua", "agua", "montanha", "montanha", "agua", "agua", 
		"montanha", "montanha", "agua", "agua", "montanha", "montanha",
	],


    [		
		"montanha", "areia", "areia", "areia", "areia", "areia", 
		"areia", "montanha", "montanha", "montanha", "montanha", "montanha",
		"grama", "grama", "floresta", "grama", "grama", "grama", 
		"grama", "grama", "floresta", "floresta", "floresta", "grama", 
		"grama", "montanha", "grama", "grama", "agua", "agua", 
		"agua", "agua", "agua", "agua", "agua", "agua", 
		"montanha", "montanha", "agua", "agua", "montanha", "montanha",
	],


    [		
		"montanha", "areia", "areia", "areia", "areia", "areia", 
		"areia", "areia", "areia", "montanha", "montanha", "montanha",
		"grama", "grama", "floresta", "grama", "agua", "agua", 
		"agua", "grama", "grama", "floresta", "grama", "grama", 
		"grama", "montanha", "grama", "grama", "agua", "agua", 
		"agua", "agua", "agua", "agua", "agua", "agua", 
		"montanha", "montanha", "agua", "agua", "montanha", "montanha",
	],


    [		
		"montanha", "areia", "areia", "areia", "areia", "areia", 
		"areia", "areia", "areia", "montanha", "montanha", "montanha",
		"grama", "grama", "floresta", "grama", "grama", "grama", 
		"grama", "grama", "grama", "floresta", "grama", "grama", 
		"grama", "montanha", "grama", "grama", "agua", "agua", 
		"agua", "agua", "agua", "agua", "agua", "agua", 
		"agua", "agua", "agua", "agua", "montanha", "montanha",
	],


    [		
		"montanha", "areia", "areia", "areia", "areia", "areia", 
		"areia", "areia", "areia", "areia", "grama", "grama", 
		"grama", "grama", "grama", "grama", "grama", "grama", 
		"grama", "grama", "grama", "grama", "grama", "grama", 
		"grama", "montanha", "montanha", "montanha", "agua", "agua", 
		"agua", "agua", "agua", "agua", "agua", "agua", 
		"agua", "agua", "agua", "agua", "montanha", "montanha",
	],



    [		
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
		"montanha", "montanha", "montanha", "montanha", "montanha", "montanha",
	],


]