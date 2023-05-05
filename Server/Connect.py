import anvil.server

anvil.server.connect('server_BV7VOL3FP6D7UWD26KIO23R7-76THGWLXYYGGHEAX')

@anvil.server.callable
def answer_question(prepro1):
  while prepro1 != 'q':
      
    prepro1 = clean_text(prepro1)
    prepro = [prepro1]

    txt = []
    for x in prepro:        
          lst = []
          for y in x.split():         
            try:
                lst.append(vocab[y])        
            except:
                lst.append(vocab['<OUT>'])
          txt.append(lst)

          txt = pad_sequences(txt, 13, padding='post')

          stat = enc_model.predict( txt )

          empty_target_seq = np.zeros( ( 1 , 1) )

          empty_target_seq[0, 0] = vocab['<SOS>']

          stop_condition = False
          decoded_translation = ''

          while not stop_condition :

              dec_outputs , h, c= dec_model.predict([ empty_target_seq] + stat )
              decoder_concat_input = dense(dec_outputs)

              sampled_word_index = np.argmax( decoder_concat_input[0, -1, :] )
            
              sampled_word = inv_vocab[sampled_word_index] + ' '

              if sampled_word != '<EOS> ':
                decoded_translation += sampled_word  

              if sampled_word == '<EOS> ' or len(decoded_translation.split()) > 13:
                stop_condition = True 

              empty_target_seq = np.zeros( ( 1 , 1 ) )  
              empty_target_seq[ 0 , 0 ] = sampled_word_index
              stat = [h, c]  
    return decoded_translation

answer_question('hello')