let fileForm1 = document.getElementById('upload-image1')
let fileForm2 = document.getElementById('upload-image2')

function handleFileSelect1(evt) {
    var files = evt.target.files;

    // Loop through the FileList and render image files as thumbnails.
    for (var i = 0, f; f = files[i]; i++) {

      // Only process image files.
      if (!f.type.match('image.*')) {
        continue;
      }

      var reader = new FileReader();

      // Closure to capture the file information.
      reader.onload = (function(theFile) {
        return function(e) {
          // Render thumbnail.
          var span = document.createElement('span');
          span.innerHTML =
          [
            '<img src="',
            e.target.result,
            '" id="uploadPhoto1" title="', escape(theFile.name),
            '"/>'
          ].join('');
          document.getElementById('photoDescription1').insertBefore(span, null);
          document.getElementById("uploadPhoto1").setAttribute("style","width:300px;height:270px");

        };
      })(f);

      // Read in the image file as a data URL.
      reader.readAsDataURL(f);
      addClass();
    }
  }

function handleFileSelect2(evt) {
    var files = evt.target.files;

    // Loop through the FileList and render image files as thumbnails.
    for (var i = 0, f; f = files[i]; i++) {

      // Only process image files.
      if (!f.type.match('image.*')) {
        continue;
      }

      var reader = new FileReader();

      // Closure to capture the file information.
      reader.onload = (function(theFile) {
        return function(e) {
          // Render thumbnail.
          var span = document.createElement('span');
          span.innerHTML =
          [
            '<img src="',
            e.target.result,
            '" id="uploadPhoto2" title="', escape(theFile.name),
            '"/>'
          ].join('');
          document.getElementById('photoDescription2').insertBefore(span, null);
          document.getElementById("uploadPhoto2").setAttribute("style","width:300px;height:270px");

        };
      })(f);

      // Read in the image file as a data URL.
      reader.readAsDataURL(f);
      addClass();
    }
  }


fileForm1.addEventListener('change', handleFileSelect1, false);
fileForm2.addEventListener('change', handleFileSelect2, false);

