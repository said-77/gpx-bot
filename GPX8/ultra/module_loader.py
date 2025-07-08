def load_optional_modules(names, logic):
    result = {}
    for name in names:
        result[name] = f"Модуль {name} обработал {len(logic)} элементов"
    return result
