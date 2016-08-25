#! /use/bin/env python
# -*- coding: utf-8 -*-
'''/* generateSintagmaProblem_6WP.py
 *
 * Copyright (C) 2016 Gian Paolo Ciceri
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.

 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.

 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
 *
 * Author:
 * 	gian paolo ciceri <gp.ciceri@gmail.com>
 *
 *
 * Release:
 *  2016.08.24 - initial release.
 *
 */
'''
 
import random
import time
import locale

import re

from sixWeeksExercises import *
from latinGrammarRules import *

locale.setlocale(locale.LC_ALL, '')

NUMEX = (48*6)+12
NUMTRY = 10000

ID = "6WP"
PERIOD = "PAG11"

PRE = ID + '-' + PERIOD + "_esercizi_"
PRE_NAME = 'EX_' + ID + '_' + PERIOD

PREAMBLE = '''#
# -*- coding: utf-8 -*-'''


RUNCODE = '''if __name__ == "__main__":
	import sys
	for item in %s:
		for word in item[3:6]:
			print(word.encode(sys.stdin.encoding).decode(sys.stdout.encoding), end=" ")
		print()
''' % (PRE_NAME,)

NOW = time.strftime('%Y%m%d-%H00')
TODAY = time.strftime('%Y.%m.%d')

PROBLEMI = PRE + NOW + ".py"


GENERE = LATIN_GENDERS
PERSONE = LATIN_PERSONS
CASI = LATIN_CASES_VOCDECL

REGOLA = (CASI,)

LESSICO = SIXWEEKS_PAG11_VOC_EX1

NUMLEX = 1


if __name__ == "__main__":
	random.seed()
	item = 0
	num = 0
	problemDict = dict()
	exDict = dict()
	fields = '("<LAT>", "<ITA>", "<ING>", "%s", "%s", "%s"),'
	while (item < NUMEX and num < NUMTRY):
		num += 1
		regola = list()
		esempio = list()
		for rule in REGOLA:
			theRule = random.choice(rule)
			regola.append(theRule[0])
			esempio.append(theRule[1])   
		lessico = list()
		while 1:
			word = random.choice(LESSICO)[0]
			if word not in lessico and len(lessico) < NUMLEX:
				lessico.append(word)
			if len(lessico) == NUMLEX:
				break
			
		regola_string = ', '.join(regola) 
		esempio_string = ', '.join(esempio) 
		lessico_string = ', '.join(lessico) 
		
		voceX = fields % (regola_string, esempio_string, lessico_string)
			
		# con questo "comprimo" i doppi spazi in uno solo
		voce = voceX.replace("  ", " ")
			
		idItem = "%s.%d" % (ID, item)
		
		try:
			p = problemDict[(voce,)]
			print(item, num, "DOPPIO:", voce)
				
		except KeyError:
			problemDict[(voce)] = (voce,)
			exDict[item] = (voce, idItem)
		item += 1
				
	pf = open(PROBLEMI, "wb")
	pf.write(bytes(PREAMBLE + "\n\n", 'UTF-8'))
	pf.write(bytes(PRE_NAME + " = [\n", 'UTF-8'))
	
	for pitem in sorted(exDict.keys()):
		problema = exDict[pitem][0]
		pf.write(bytes(problema + "\n", 'UTF-8'))
	
	pf.write(bytes("]\n", 'UTF-8'))
	pf.write(bytes("\n\n" + RUNCODE + "\n\n", 'UTF-8'))
	
	pf.close()
		
