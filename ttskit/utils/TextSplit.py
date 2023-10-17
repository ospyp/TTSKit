"""
TTSKit by mrfakename

Copyright (c) 2023 by mrfakename. All rights reserved.
This software may be used and redistributed under the terms of the NOSCL-C-2.0 software license. A copy of this license should be provided with this software.

===

TTSKit Additional Utilities by mrfakename. TTSKit Additional Utilities is part of TTSKit. TTSKit Additional Utilities is licensed under the NOSCL-NC-2.0 software license, available with TTSKit.

TTSKit Additional Utilities is Copyright (c) 2023 by mrfakename. All rights reserved.

TextSplit is part of TTSKit Additional Utilities.
"""

from nltk import sent_tokenize
import re
class TextSplit:
    def _split_sentence(self, sentence, max_chars):
        fragments = re.split(r'([.!?;,:])', sentence)
        result = []
        current_fragment = ""
        for fragment in fragments:
            if len(current_fragment) + len(fragment) <= max_chars:
                current_fragment += fragment
            else:
                if len(fragment) > max_chars:
                    sub_fragments = re.split(r'(\s+)', fragment)
                    for sub_fragment in sub_fragments:
                        if len(current_fragment) + len(sub_fragment) <= max_chars:
                            current_fragment += sub_fragment
                        else:
                            result.append(current_fragment.strip())
                            current_fragment = sub_fragment
                else:
                    result.append(current_fragment.strip())
                    current_fragment = fragment
        if current_fragment:
            result.append(current_fragment.strip())
        cleaned_result = [re.sub(r'^[.,!?;,:]+|[.,!?;,:]+$', '', item) for item in result if not re.match(r'^[.,!?;,:]+$', item)]
        cleaned_result = [item for item in cleaned_result if item.strip() != ""]
        final_result = []
        for item in cleaned_result:
            if len(item) > max_chars:
                for i in range(0, len(item), max_chars):
                    chunk = item[i:i + max_chars]
                    final_result.append(chunk)
            else:
                final_result.append(item)
        return final_result

    def split(self, text, max_len=500):
        sents = sent_tokenize(text)
        result = []
        for sent in sents:
            if len(sent) > max_len:
                result.append(self._split_sentence(sent, max_len))
            else:
                result.append(sent)
        return result
