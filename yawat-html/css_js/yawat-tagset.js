// This file is part of the YAWAT package.
// (c) 2007 Ulrich Germann. All rights reserved.
// This is NOT free software, but permission is granted to use this 
// software free of charge for academic research purposes.

var isBilingualLabel = new Object();
var biLabels = new Object(); // tags and descriptions for bilingual groups
var moLabels = new Object(); // tags and descriptions for monolingual groups

biLabels['literal']  = 'literal';
biLabels['equivalence']  = 'equivalence'; 
biLabels['transposition'] = 'transposition';
biLabels['modulation']  = 'modulation';
biLabels['modulation_transposition'] = 'modulation_transposition';
biLabels['generalization'] = 'generalization';
biLabels['particularization']  = 'particularization';
biLabels['figurative']   = 'figurative';
biLabels['lexical_shift'] = 'lexical_shift';
biLabels['uncertain'] = 'uncertain';
biLabels['translation_error'] = 'translation_error';

//modif-type labels
//biLabels['normalisationL']   = 'Normalisation de langue';
//biLabels['reecritureFaibleVariationSem']   = 'Réécriture à faible variation sémantique';
//biLabels['reecritureForteVariationSem']   = 'Réécriture à forte variation sémantique';

////Fonctions relatives au type: Normalisation de langue
//biLabels['incorrectionContextuelle']  = 'Incorrection contextuelle';
//biLabels['incorrection']   = 'Incorrection: non-mot';
//biLabels['typographie']   = 'Typographie';

//Fonctions relatives au type: Réécriture à faible variation sémantique
//biLabels['precisionSens']   = 'Précision de sens';
//biLabels['reformulationForme']   = 'Reformulation de forme';
//biLabels['perteInfo']= 'Perte d\'information';

//Fonctions relatives au type: Réécriture à forte variation sémantique
//biLabels['reformulationSens']   = 'Reformulation de sens';
//biLabels['vandalisme']   = 'Vandalisme';

defaultBiLabel = 'literal';

moLabels['unaligned_reduction'] = 'unaligned_reduction';
moLabels['unaligned_explicitation'] = 'unaligned_explicitation';
defaultMoLabel = 'unaligned';

