
//提交回复
function Post() {
    var questionId = $('#input_id').val();
    var commentTxt =$('#comment_id').val();
    commentToTarget(questionId,1,commentTxt);
}

function commentToTarget(targetId,type,content) {
    if (!content){
        alert("回复内容为空！！！！");
        return;
    }
    $.ajax({
        type:"POST",
        url:"/comment",
        contentType:'application/json',
        data:JSON.stringify({
            "parentId":targetId,
            "content":content,
            "type":type
        }),
        success:function (response) {
            if(response.code === 200){
                window.location.reload();
                // $("#comment_section").hide();
            }else{
                if (response.code === 200){
                    var isAccepted = confirm(response.message);
                    if (isAccepted){
                        window.open("http://github.com/login/oauth/authorize?client_id=b3b546e022ca3539a8bb&redirect_url=http://localhost:8080/callback&scope=user&state=1");
                        window.localStorage.setItem("closable",true);
                    }
                }else{
                    alert(response.message);
                }

            }
        },
        dataType:"json"
    });

}

function comment(e) {
    var id =  e.getAttribute("data-id");
    var content = $('#input-'+id).val();
    commentToTarget(id,2,content);
}

//取消评论
function close(e) {
    let id =e.getAttribute("data-id");
    var comments =$("#comment-"+id);
    comments.removeClass("in");
}


//显示二级回复
function collapseComments(e) {
    let id =e.getAttribute("data-id");
    var comments =$("#comment-"+id);
    // // comments.toggleClass("in");
    // if (comments.hasClass("in")){
    //     comments.removeClass("in");
    // }else{
    //     $.getJSON("/comment/"+id,function (data) {
    //         console.log(data);
    //         comments.addClass("in");
    //     });
    // }

    //获取一下二级评论展开状态
    var collapse = e.getAttribute("data-collapse");
    if (collapse){
        comments.removeClass("in");
        e.removeAttribute("data-collapse");
        e.classList.remove("active");
    }else{

        $.getJSON("/comment/" + id, function (data) {
            console.log(data);
            var commentBody = $("#comment-" + id);
            // console.log(commentBody);
            
            $.each(data.data, function (index, comments) {
                console.log(index);
                var c = $("<div/>", {
                    "class": "col-lg-12 col-md-12 col-sm-12 col-xs-12",
                    html: comments.content
                });
                commentBody.prepend(c);
            });

            //展开二级评论
            comments.addClass("in");
            //标记二级评论状态
            e.setAttribute("data-collapse","in");
            e.classList.add("active");
        });
    }
}
