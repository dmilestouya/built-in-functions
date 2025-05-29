import streamlit as st
import random
import builtins
import inspect
import io
import contextlib

# Funciones built-in filtradas (excluye errores y warnings)
builtin_funcs = [name for name in dir(builtins) if isinstance(getattr(builtins, name), type(abs))]

# Ejemplos seguros y demostrativos
examples = {
    "abs": "abs(-7)",
    "all": "all([True, True, False])",
    "any": "any([False, False, True])",
    "ascii": "ascii('ñ')",
    "bin": "bin(10)",
    "bool": "bool(0)",
    "bytearray": "bytearray('hola', 'utf-8')",
    "bytes": "bytes('hola', 'utf-8')",
    "callable": "callable(len)",
    "chr": "chr(97)",
    "complex": "complex(2, 3)",
    "dict": "dict(a=1, b=2)",
    "divmod": "divmod(9, 4)",
    "enumerate": "list(enumerate(['a', 'b', 'c']))",
    "filter": "list(filter(lambda x: x > 0, [-1, 0, 1, 2]))",
    "float": "float('3.14')",
    "format": "format(0.5, '.1%')",
    "frozenset": "frozenset([1, 2, 3])",
    "getattr": "getattr(str, 'upper')('hola')",
    "hasattr": "hasattr(str, 'lower')",
    "hash": "hash('abc')",
    "hex": "hex(255)",
    "id": "id(object())",
    "int": "int('42')",
    "isinstance": "isinstance(5, int)",
    "issubclass": "issubclass(bool, int)",
    "iter": "iter([1, 2, 3])",
    "len": "len('Python')",
    "list": "list((1, 2, 3))",
    "map": "list(map(str.upper, ['a', 'b']))",
    "max": "max([5, 3, 9])",
    "min": "min([5, 3, 9])",
    "next": "next(iter(['a', 'b']))",
    "object": "object()",
    "oct": "oct(8)",
    "ord": "ord('a')",
    "pow": "pow(2, 3)",
    "range": "list(range(3))",
    "repr": "repr('Hola')",
    "reversed": "list(reversed([1, 2, 3]))",
    "round": "round(3.14159, 2)",
    "set": "set([1, 2, 2, 3])",
    "slice": "list(range(10))[slice(2, 8, 2)]",
    "sorted": "sorted([3, 1, 2])",
    "str": "str(123)",
    "sum": "sum([1, 2, 3])",
    "tuple": "tuple([1, 2, 3])",
    "type": "type('hola')",
    "zip": "list(zip([1, 2], ['a', 'b']))",
}

# Estado de sesión
if 'show_doc' not in st.session_state:
    st.session_state.show_doc = False
if 'current_func' not in st.session_state:
    st.session_state.current_func = None

# Título
#st.title("Python: Funciones Integradas")
st.markdown("<h1 style='color: green;'>Python: Funciones Integradas</h1>", unsafe_allow_html=True)

st.markdown("<p style='color: green;'>El objetivo es simplemente visualizar distintas <code>built-in-functions</code></p1>", unsafe_allow_html=True)
st.markdown("<ul style='color: green;line-height: .5;'><li>Sus parámetros</li><br><li>Qué hacen</li></ul>", unsafe_allow_html=True)


# Botón para elegir función aleatoria
if st.button("🎲: Teclear para elegir una built-in function"):
    st.session_state.current_func = random.choice(builtin_funcs)
    st.session_state.show_doc = True

# Mostrar función seleccionada
if st.session_state.show_doc and st.session_state.current_func:
    func_name = st.session_state.current_func
    func_obj = getattr(builtins, func_name)

    st.subheader(f"`{func_name}()`")

    doc = inspect.getdoc(func_obj) or "No hay documentación disponible."
    st.code(doc, language='markdown')

    doc_url = f"https://docs.python.org/es/3.13/library/functions.html#{func_name}"
    st.markdown(f"[🔗 Link a Documentación de `{func_name}()`]({doc_url})", unsafe_allow_html=True)

    if func_name in examples:
        st.markdown("<b style='color:#6082B6'>Ejemplo:</b>", unsafe_allow_html=True)
        st.code(examples[func_name], language='python')

        #st.markdown("**Resultado al ejecutar el ejemplo:**")
        st.markdown("<b style='color:#6082B6'>Resultado al ejecutar el ejemplo:</b>", unsafe_allow_html=True)
	
        with contextlib.redirect_stdout(io.StringIO()) as f:
            try:
                result = eval(examples[func_name])
                if result is not None:
                    print(result)
            except Exception as e:
                print(f"❌ Error al ejecutar el ejemplo: {e}")
        st.text(f.getvalue())
    else:
        st.info("No hay ejemplo disponible para esta función.")

    # Botón para cerrar
    #if st.button("❌ Cerrar función"):
    #    st.session_state.show_doc = False
    #    st.session_state.current_func = None
    #    st.experimental_rerun()
