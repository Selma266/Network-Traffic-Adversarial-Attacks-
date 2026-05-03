
# PREDICATE représente une fonction de validation. Elle prend un tuple de valeurs numériques, par exemple (x1, x2, x3), et retourne True si la contrainte est respectée, False sinon.
# Ce fichier définit les types de données utilisés par CGE. Il explique surtout le format des contraintes constraints = {constraint_id: ((feature_indices), predicate)}
# 
"""
Predicate is a function from seq R -> bool.

Cela signifie :
un prédicat prend une séquence de nombres réels
et retourne un booléen : True ou False.
"""
# CONSTR_DICT représente le dictionnaire complet des contraintes.
# Structure :  {id_contrainte: ((indices_features),predicate_ou_bool)}
# - La clé peut être n’importe quel identifiant : int, str, etc.
# - Le premier élément est un tuple d’indices de features.
# - Le deuxième élément est :
#     soit une fonction prédicat,
#     soit False pour indiquer une feature immutable.
from typing import Dict, Callable, Tuple, Union, Any

PREDICATE = Callable[[Tuple[float, ...]], bool]
"""Predicate is a function from seq R -> bool."""

CONSTR_DICT = Dict[Any, Tuple[Tuple[int, ...], Union[PREDICATE, bool]]]
"""Constraints dictionary type.

   * The key is a uid
   * The value is a pair of:
     - a non-empty tuple of source feature indices
     - a predicate (a function to evaluate feature validity
       based on source values), or a Boolean.
"""
class Validatable:
    """Base class for an attack with constraints"""
    cge = None

    def vhost(self):
        """validation model owner"""
        return self
