#
# -*- coding: utf-8 -*-
'''/* latinGrammarRules.py
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
 *  2016.08.17 - initial release. only to run the vala-equivalent of sample-mdb.c
 *
 */
'''

# ā ă ē ĕ ī ĭ ō ū ŭ ŏ
#
# ('', '', '')

LATIN_CASES_VOCDECL = [
('NOM_SING', 'lupus/rosă/bellum'),
('GEN_SING', 'lupi/rosae/belli'),
('DAT_SING', 'lupo/rosae/bello'),
('ACC_SING', 'lupum/rosam/bellum'),
('VOC_SING', 'lupe/rosă/bellum'),
('ABL_SING', 'lupo/rosā/bello'),
('NOM_PLUR', 'lupi/rosae/bella'),
('GEN_PLUR', 'luporum/rosarum/bellorum'),
('DAT_PLUR', 'lupis/rosis/bellis'),
('ACC_PLUR', 'lupos/rosas/bella'),
('VOC_PLUR', 'lupi/rosae/bella'),
('ABL_PLUR', 'lupis/rosis/bellis'),
]

LATIN_CASES_CONSDECL = [
('NOM_SING', 'consul/civis/animal'),
('GEN_SING', 'consulis/civis/animalis'),
('DAT_SING', 'consuli/civi/animali'),
('ACC_SING', 'consulem/civem/animal'),
('VOC_SING', 'consul/civis/animal'),
('ABL_SING', 'consule/cive/animali'),
('NOM_PLUR', 'consules/cives/animalia'),
('GEN_PLUR', 'consulum/civium/animalium'),
('DAT_PLUR', 'consulibus/civibus/animalibus'),
('ACC_PLUR', 'consules/cives/animalia'),
('VOC_PLUR', 'consules/cives/animalia'),
('ABL_PLUR', 'consulibus/civibus/animalibus'),
]


LATIN_GENDERS = [
('MASC', 'puer'),
('FEMM', 'puella'),
('NEUT', 'bellum'),
]

LATIN_PERSONS = [
('I_SING', 'amo'),
('II_SING', 'amas'),
('III_SING', 'amat'),
('I_SING', 'amamus'),
('II_SING', 'amatis'),
('III_SING', 'amant'),
]
