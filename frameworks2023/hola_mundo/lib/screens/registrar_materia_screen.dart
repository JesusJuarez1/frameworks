import 'package:flutter/material.dart';

class RegistrarMateria extends StatefulWidget {
  const RegistrarMateria({super.key});

  final String title = "Registrar Materia";

  @override
  State<RegistrarMateria> createState() => _RegistrarMateria();
}

class _RegistrarMateria extends State<RegistrarMateria> {
  // ignore: unused_field
  late String _clave;
  // ignore: unused_field
  late String _nombre;
  late int _creditos;
  // ignore: unused_field
  late String _semestre = '1er. Semestre';
  // ignore: unused_field
  late bool _optativa = false;
  // ignore: unused_field
  late String _programa;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: ListView(children: <Widget>[
        Column(
            mainAxisAlignment: MainAxisAlignment.center,
            mainAxisSize: MainAxisSize.min,
            children: [
              const SizedBox(
                child: Divider(color: Colors.blueGrey),
              ),
              TextField(
                autofocus: true,
                textCapitalization: TextCapitalization.characters,
                decoration: InputDecoration(
                    labelText: 'Clave:',
                    suffixIcon: Icon(Icons.key),
                    border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10.0))),
                onSubmitted: (valor) {
                  _clave = valor;
                  print(_clave);
                },
              ),
              const Divider(
                height: 10.0,
              ),
              TextField(
                autofocus: true,
                textCapitalization: TextCapitalization.characters,
                decoration: InputDecoration(
                    labelText: 'Nombre de la materia:',
                    suffixIcon: const Icon(Icons.book_rounded),
                    border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10.0))),
                onSubmitted: (valor) {
                  _nombre = valor;
                  print(_nombre);
                },
              ),
              const Divider(
                height: 10.0,
              ),
              TextFormField(
                  keyboardType: TextInputType.number,
                  decoration: InputDecoration(
                      labelText: 'Creditos:',
                      suffixIcon: const Icon(Icons.book_rounded),
                      border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(10.0))),
                  onSaved: (valor) {
                    _creditos = valor as int;
                    print(_creditos);
                  }),
              const Divider(
                height: 10.0,
              ),
              DropdownButton(
                items: <String>[
                  '1er. Semestre',
                  '2do. Semestre',
                  '3er. Semestre',
                  '4to. Semestre',
                  '5to. Semestre',
                  '6to. Semestre',
                  '7mo. Semestre',
                  '8vo. Semestre',
                  '9no. Semestre'
                ].map((String value) {
                  return DropdownMenuItem<String>(
                    value: value,
                    child: Text(value),
                  );
                }).toList(),
                value: _semestre,
                hint: const Text('Escoge un semestre'),
                onChanged: (valor) {
                  setState(() {
                    _semestre = valor!;
                  });
                },
                icon: const Icon(Icons.perm_contact_calendar),
                isExpanded: true,
              ),
              const Divider(
                height: 10.0,
              ),
              SwitchListTile(
                title: const Text('¿Optativa?'),
                value: _optativa,
                onChanged: (valor) {
                  setState(() {
                    _optativa = valor;
                  });
                },
                subtitle: _optativa ? const Text('Sí') : const Text('No'),
              ),
              const Divider(
                height: 10.0,
              ),
              TextFormField(
                  keyboardType: TextInputType.text,
                  decoration: InputDecoration(
                      labelText: 'Programa:',
                      suffixIcon: const Icon(Icons.book_rounded),
                      border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(10.0))),
                  onSaved: (valor) {
                    _programa = valor!;
                    print(_programa);
                  }),
              const Divider(
                height: 10.0,
              ),
              TextButton(
                  style: TextButton.styleFrom(
                      backgroundColor: Colors.blue,
                      textStyle: const TextStyle(fontSize: 20)),
                  onPressed: _registrarMateria,
                  child: const Text('guardar',
                      style: const TextStyle(color: Colors.white)))
            ]),
      ]),
    );
  }

  void _registrarMateria() {
    print('$_clave $_nombre');
  }
}
