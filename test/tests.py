doc_correct = [{
       "model": "clio",
       "brand": "renault",
       "category": {
           "name": "common",
           "discountTax": 60   
       },
       "passengers": 5,
       "year": 2018,
       "price": 20,
       "available": True,
   }
]

doc_incorrect1 = [{
       "model": "clio",
       "brand": "seat",
       "category": {
           "name": "common",
           "discountTax": 60   
       },
       "passengers": 5,
       "year": 2050,
       "price": 20,
       "available": True,
   }
]

doc_correct_classic = [{
       "model": "mustang",
       "brand": "ford",
       "category": {
           "name": "classic",
           "discountTax": 40
       },
       "passengers": 5,
       "year": 1998,
       "price": 65,
       "available": True,
   }

]


#BBDD_connect comprobar que se conecta a la base de datos
#BBDD_query_lte comprobar que no nos da ningun documento que el valor sea mayor que 25