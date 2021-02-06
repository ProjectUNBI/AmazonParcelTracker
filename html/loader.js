/*
	Produced 2019
	By https://github.com/amattu2
	Copy Alec M.
	License GNU Affero General Public License v3.0
*/

var el = document.getElementById('mylist');

function setProgress(bar, progressvalue, textcontent, status = "") {
    // Checks
    progress = parseFloat(progressvalue).toFixed(0);
    if (progress < 0 || progress > 100) {
        return false
    }
    if (typeof (status) !== "string") {
        status = ""
    }

    // UI
    bar.dataset.progress = progress.toString();
    textcontent.textContent = status;
}

function getHtmlPropValue(prop,value){
    var para = document.createElement('p');
    para.insertAdjacentHTML('beforeend',"<p><b>"+prop+"</b>"+value+"</p>")
    return para
}

//////////////////////////Updater///////////////////

function mycallback(datastr) {
    console.log(datastr);
    var data = JSON.parse(datastr);
    var url_loaded_time = undefined;

    var buttuns_dom = el.lastChild;
    el.removeChild(el.lastChild)
    for (var i = 0; i < data.length; i++) {
        var order_amazon = data[i]
        if (url_loaded_time == undefined) {
            url_loaded_time = order_amazon["loaded_time_of_url_human_readable"]
        }
        //////////////Progresss calculating///////////

        var track_progress = order_amazon["track_progress"]

        var progress = 0
        var flag_skip_this_order = true;
        var last_location_str = ""
        for (var prop in track_progress) {
            if (prop == "Delivered today") {
                flag_skip_this_order = false;
                progress = 100;
                last_location_str = prop
                break
            }
            if (prop == "ORDERED") {
                flag_skip_this_order = false;
                continue
            }
            if (prop == "SHIPPED") {
                flag_skip_this_order = false;
                if (track_progress["SHIPPED"]) {
                    progress = progress + 50
                }
                continue
            }
            if (prop == "OUT_FOR_DELIVERY") {
                flag_skip_this_order = false;
                if (track_progress["OUT_FOR_DELIVERY"]) {
                    progress = progress + 40
                }
                continue
            }
            if (prop == "DELIVERED") {
                if (track_progress["DELIVERED"]) {
                    flag_skip_this_order = false;
                    progress = 100;
                }
                break
            }

        }
        if (flag_skip_this_order) {
            continue
        }

        //////////////////////////////////////////////


        var is_out_for_delivery = order_amazon["is_out_for_deliver"]
        var has_error_loading = order_amazon["has_error_loading"]

        var load_time = order_amazon["loaded_time_human_readable"]
        var order_name = order_amazon["order_name"]
        var order_id = order_amazon["order_id"]
        var address = order_amazon["where_to_deliver"]

        var last_location = order_amazon["last_tract_location"]
        if (last_location_str === "") {
            for (j = 0; j < last_location.length; j++) {
                last_location_str = "\n" + last_location[j]
            }
        }

        var node = document.createElement("li");
        var div = document.createElement('div');
        div.className = 'loader-case';
        var div_progress = document.createElement('div');
        div_progress.className = 'progress-case';

        var div_progress_status = document.createElement('div');
        div_progress_status.className = 'progress-status';

        var div_progress_bar = document.createElement('div');
        div_progress_bar.className = 'progress-bar';

        setProgress(div_progress_bar, progress, div_progress_status, last_location_str)

        var div_detail=document.createElement("div")
        div_detail.align="left"
        div_detail.appendChild(getHtmlPropValue("Loaded time: ",load_time))
        div_detail.appendChild(getHtmlPropValue("No error: ",!has_error_loading.toString()))
        div_detail.appendChild(getHtmlPropValue("Order Id: ",order_id))
        for (l=0;l<order_name.length;order_name++){
            div_detail.appendChild(getHtmlPropValue((l+1).toString()+") ",order_name))
        }
        div_progress.appendChild(div_detail)
        div_progress.append(div_progress_status)
        div_progress.append(div_progress_bar)
        div.append(div_progress)
        node.appendChild(div);
        var para = document.createElement("p");
        node.appendChild(para)
        el.appendChild(node);
    }
    el.appendChild(getHtmlPropValue("Url load time: ",url_loaded_time))
}

function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

httpGetAsync("amazon", mycallback);


/////////////////////////Turn off alarm////////////////

function clickturnoff() {
    // body...
    console.log("Click");
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            console.log("Succes fully sent turn off intent");
        }
    }
    xmlHttp.open("GET", "offalarm", true); // true for asynchronous 
    xmlHttp.send(null);
}

function reset() {
    console.log("Click");
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            console.log("Succes fully sent reset intent");
            resetbtn.textContent = "Reset done";
        }
    }
    xmlHttp.open("GET", "reset", true); // true for asynchronous 
    xmlHttp.send(null);
}


