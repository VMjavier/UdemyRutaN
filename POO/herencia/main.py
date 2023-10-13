import clases

pokemon = clases.Pokemon()

pokemon.setNombre("Blastoise")
pokemon.setAtaque(83)
pokemon.setDefensa(100)
pokemon.setSalud(79)
pokemon.setTipo("Agua")

print(f"El pokemon es {pokemon.getNombre()} y es de tipo {pokemon.getTipo()}.")

pokemon2 = clases.Region()
pokemon2.setNombre("Pikachu")
pokemon2.setAtaque(55)
pokemon2.setDefensa(40)
pokemon2.setSalud(35)
pokemon2.setTipo("Eléctrico")


print(f"El pokemon es {pokemon2.getNombre()} y es de tipo {pokemon2.getTipo()}.")
print(f"Y tiene ataque especial {pokemon2.getAtaqueEspecial()}.")