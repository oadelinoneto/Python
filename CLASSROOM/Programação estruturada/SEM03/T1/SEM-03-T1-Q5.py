po_de_lua = int(input())
essencia_de_dragao = int(input())
lagrima_fenix = int(input())

if po_de_lua == 0 and essencia_de_dragao == 0 and lagrima_fenix == 0: 
    pass
else:
    custo = (po_de_lua*5) + (essencia_de_dragao*3) + (lagrima_fenix*8)
    print(custo)