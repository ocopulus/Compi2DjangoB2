import ply.yacc as yacc
import ply.lex as lex

class Com:

    def __init__(self):
        self.login = False
        self.tablas = None
        self.ejecucion = None
        self.mensajes = None
        self.historial = None
        tokens = ('CADENA', 'NUMERO', 'VER', 'FAL', 'CODIGO', 'CCOR',
                  'ACOR', 'COMA', 'DOSP')

        #Tokens
        t_VER = r'true'
        t_FAL = r'false'
        t_ACOR = r'\['
        t_CCOR = r'\]'
        t_COMA = r','
        t_DOSP = r':'

        def t_CADENA(t):
            r'"(\\"|[^"])*"'
            return t

        def t_NUMERO(t):
            r'\d+'
            try:
                t.value = int(t.value)
            except ValueError:
                print("Integer value too large %d", t.value)
                t.value = 0
            return t

        def t_CODIGO(t):
            r'%% ([^%])* %%'
            t.value = t.value.replace('%%','')
            return t

        # Ignored characters
        t_ignore = " \t"

        def t_newline(t):
            r'\n+'
            t.lexer.lineno += t.value.count("\n")

        def t_error(t):
            print("Illegal character '%s'" % t.value[0])
            t.lexer.skip(1)

        self.lexer = lex.lex()

        # dictionary of names y Para poner glovales
        self.names = { }

        def p_inicio(t):
            'inicio : json'
            #print('exito papu')

        def p_json(t):
            'json : ACOR contenido CCOR'

        def p_contenido(t):
            'contenido : contenido COMA CADENA DOSP valor'
            accion = t[3].replace('"','')
            val = t[5]
            if accion == 'login':
                if val == True:
                    self.login = True
                else:
                    self.login = False
            if accion == 'tablas':
                self.tablas = val
            if accion == 'ejecucion':
                self.ejecucion = val
            if accion == 'mensajes':
                self.mensajes = val
            if accion == 'historial':
                self.historial = val

        def p_contenido_2(t):
            'contenido : CADENA DOSP valor'
            accion = t[1].replace('"','')

        def p_valor(t):
            'valor : CADENA'
            t[0] = t[1].replace('"','')

        def p_valor2(t):
            'valor : json'
            t[0] = t[1]

        def p_valor3(t):
            'valor : NUMERO'
            t[0] = t[1]

        def p_valor4(t):
            'valor : CODIGO'
            t[0] = t[1].replace('%%','')

        def p_valor5(t):
            'valor : VER'
            t[0] = True

        def p_valor6(t):
            'valor : FAL'
            t[0] = False

        def p_error(t):
            if t:
                print("Syntax error at '%s'" % t.value)
                self.parser.restart()
            else:
                print("Syntax error at EOF")
                self.parser.restart()

        self.parser = yacc.yacc()

    def accion(self, cod):
        self.parser.parse(cod)
