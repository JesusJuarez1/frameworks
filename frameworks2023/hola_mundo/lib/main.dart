import 'package:flutter/material.dart';
import 'package:hola_mundo/screens/registrar_materia_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      //debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const ContadorScreen(title: 'Flutter Home Page'),
    );
  }
}

class ContadorScreen extends StatefulWidget {
  const ContadorScreen({super.key, required this.title});

  final String title;

  @override
  State<ContadorScreen> createState() => _ContadorScreen();
}

class _ContadorScreen extends State<ContadorScreen> {
  int _contador = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_contador',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
      ),
      floatingActionButton: Row(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          FloatingActionButton(
            onPressed: _incrementarContador,
            tooltip: 'Increment',
            child: const Icon(Icons.add),
          ),
          FloatingActionButton(
            onPressed: _resetearContador,
            tooltip: 'Reset',
            child: const Icon(Icons.reset_tv),
          ),
          FloatingActionButton(
            onPressed: _decrementarContador,
            tooltip: 'Decrement',
            child: const Icon(Icons.minimize),
          ),
          FloatingActionButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                    builder: (context) => const RegistrarMateria()),
              );
            },
            tooltip: 'Registrar Materia',
            child: const Icon(Icons.account_balance_wallet_outlined),
          )
        ],
      ),
    );
  }

  void _incrementarContador() {
    setState(() {
      _contador++;
    });
  }

  void _resetearContador() {
    setState(() {
      _contador = 0;
    });
  }

  void _decrementarContador() {
    setState(() {
      _contador--;
    });
  }
}
