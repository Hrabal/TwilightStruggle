# -*- coding: utf-8 -*-
import os
module_path = os.path.dirname(os.path.abspath(__file__))
models = [f for f in os.listdir(module_path) if f.endswith('.py') and f not in ('__init__.py', 'dbtools.py')]
__all__ = models
print('Imported models: %s' % ', '.join(models) if models else 'No models avaiable in the models directory.')
