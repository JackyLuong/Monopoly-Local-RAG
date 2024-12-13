  $("#send_query").on("click", function(){
    question = $("#message_question").val();
    queryLLM(question);
  });

  async function queryLLM(question){
    let query = await eel.queryLLM(question)();
    let html = '<div class="row">';
          html += '<div class="col-2"></div>';

          html += '<div class="col-8">';
          html += '<p>'+ query +'</p>';
          html += '</div>';

          html += '<div class="col-2"></div>';

        html += '</div>';
    
 
    $("#response-box").html(html);
  };