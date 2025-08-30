jQuery(document).ready(function($) {
  "use strict";

  // Contact Form Submission
  $('form.contactForm').submit(function(e) {
    e.preventDefault(); // prevent default form submission

    var f = $(this).find('.form-group'),
        ferror = false,
        emailExp = /^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i;

    // Validate input fields
    f.children('input').each(function() {
      var i = $(this);
      var rule = i.attr('data-rule');

      if (rule !== undefined) {
        var ierror = false;
        var pos = rule.indexOf(':', 0);
        if (pos >= 0) {
          var exp = rule.substr(pos + 1);
          rule = rule.substr(0, pos);
        }

        switch (rule) {
          case 'required':
            if (i.val() === '') ierror = ferror = true;
            break;
          case 'minlen':
            if (i.val().length < parseInt(exp)) ierror = ferror = true;
            break;
          case 'email':
            if (!emailExp.test(i.val())) ierror = ferror = true;
            break;
          case 'checked':
            if (!i.is(':checked')) ierror = ferror = true;
            break;
          case 'regexp':
            exp = new RegExp(exp);
            if (!exp.test(i.val())) ierror = ferror = true;
            break;
        }

        i.next('.validation').html(ierror ? (i.attr('data-msg') || 'wrong input') : '').show('blind');
      }
    });

    // Validate textarea
    f.children('textarea').each(function() {
      var i = $(this);
      var rule = i.attr('data-rule');

      if (rule !== undefined) {
        var ierror = false;
        var pos = rule.indexOf(':', 0);
        if (pos >= 0) {
          var exp = rule.substr(pos + 1);
          rule = rule.substr(0, pos);
        }

        switch (rule) {
          case 'required':
            if (i.val() === '') ierror = ferror = true;
            break;
          case 'minlen':
            if (i.val().length < parseInt(exp)) ierror = ferror = true;
            break;
        }

        i.next('.validation').html(ierror ? (i.attr('data-msg') || 'wrong input') : '').show('blind');
      }
    });

    if (ferror) return false;

    var str = $(this).serialize();
    var action = $(this).attr('action') || '/contact'; // Flask endpoint

    // Send AJAX POST request
    $.ajax({
      type: "POST",
      url: action,
      data: str,
      success: function(msg) {
        if (msg === 'OK') {
          $("#sendmessage").addClass("show");
          $("#errormessage").removeClass("show");
          $('.contactForm').find("input, textarea").val("");
        } else {
          $("#sendmessage").removeClass("show");
          $("#errormessage").addClass("show");
          $('#errormessage').html(msg);
        }
      },
      error: function(xhr, status, error) {
        $("#sendmessage").removeClass("show");
        $("#errormessage").addClass("show");
        $('#errormessage').html("Something went wrong: " + error);
      }
    });

    return false;
  });
});
