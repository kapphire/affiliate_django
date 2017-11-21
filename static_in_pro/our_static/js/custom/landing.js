let MoreArticles = (() => {
	let count = 2;
	const _baseUrl = '';
	const send_request = (endpoint, params, callback) => {
		$.ajax({
			url : _baseUrl + endpoint,
			data : params,
			dataType : 'json',
			type : "POST",
			success : (response) => {
				if (!response.status) {
					alert('Please declare response.status...')
				}else if (typeof callback === 'function'){
					callback(response);
				}
			},
			error : (error) => {
				alert("Something went wrong...");
			}
		})
	}

	const moreArticles = (val) => {
		send_request("/", {"val" : val}, (response) => {
			gambling = JSON.parse(response.latest_posts['gambling_latest']);
			affiliate = JSON.parse(response.latest_posts['affiliate_latest']);
			forex = JSON.parse(response.latest_posts['forex_latest']);
			let img_url = document.URL + 'static/img/'
			let selector = $('.blog').find("article").filter(':last').parent();

			let gambling_publish = new Date(gambling[0].fields.publish)
			let affiliate_publish = new Date(affiliate[0].fields.publish)
			let forex_publish = new Date(forex[0].fields.publish)
			gambling_get_absolute_url = document.URL + 'blog/' + gambling[0].fields.classify + '/' + gambling_publish.getUTCFullYear() + '/' + (gambling_publish.getUTCMonth() + 1) + '/' + gambling_publish.getUTCDate() + '/' + gambling[0].fields.slug
			affiliate_get_absolute_url = document.URL + 'blog/' + affiliate[0].fields.classify + '/' + affiliate_publish.getUTCFullYear() + '/' + (affiliate_publish.getUTCMonth() + 1) + '/' + affiliate_publish.getUTCDate() + '/' + affiliate[0].fields.slug
			forex_get_absolute_url = document.URL + 'blog/' + forex[0].fields.classify + '/' + forex_publish.getUTCFullYear() + '/' + (forex_publish.getUTCMonth() + 1) + '/' + forex_publish.getUTCDate() + '/' + forex[0].fields.slug

			
			selector.after('<div class="col-md-4"><article class="blog-post"><figure><a href="' + img_url + gambling[0].fields.image_gambling + '" class="single_image"><div class="blog-img-wrap"><div class="overlay"><i class="fa fa-search"></i></div><img src="' + img_url + gambling[0].fields.image_gambling + '" alt="' + gambling[0].fields.title + '"/></div></a><figcaption><h2><a href="' + gambling_get_absolute_url + '" class="blog-category" data-toggle="tooltip" data-placement="top" data-original-title="See more posts">' + gambling[0].fields.title + '</a></h2><p><a href="' + gambling_get_absolute_url + '" class="blog-post-title">View <i class="fa fa-angle-right"></i></a></p></figcaption></figure></article></div>');
			selector.after('<div class="col-md-4"><article class="blog-post"><figure><a href="' + img_url + affiliate[0].fields.image_affiliate + '" class="single_image"><div class="blog-img-wrap"><div class="overlay"><i class="fa fa-search"></i></div><img src="' + img_url + affiliate[0].fields.image_affiliate + '" alt="' + affiliate[0].fields.title + '"/></div></a><figcaption><h2><a href="' + affiliate_get_absolute_url + '" class="blog-category" data-toggle="tooltip" data-placement="top" data-original-title="See more posts">' + affiliate[0].fields.title + '</a></h2><p><a href="' + affiliate_get_absolute_url + '" class="blog-post-title">View <i class="fa fa-angle-right"></i></a></p></figcaption></figure></article></div>');
			selector.after('<div class="col-md-4"><article class="blog-post"><figure><a href="' + img_url + forex[0].fields.image_forex + '" class="single_image"><div class="blog-img-wrap"><div class="overlay"><i class="fa fa-search"></i></div><img src="' + img_url + forex[0].fields.image_forex + '" alt="' + forex[0].fields.title + '"/></div></a><figcaption><h2><a href="' + forex_get_absolute_url + '" class="blog-category" data-toggle="tooltip" data-placement="top" data-original-title="See more posts">' + forex[0].fields.title + '</a></h2><p><a href="' + forex_get_absolute_url + '" class="blog-post-title">View <i class="fa fa-angle-right"></i></a></p></figcaption></figure></article></div>');
		});
	}

	const init = () => {
		$(document)
		.on("click", "#more_articles", (event) => {
			event.preventDefault();
			let val = count++;
			moreArticles(val);
		})
	}

	return {
		init : init
	}
})();

((window, $) => {
	MoreArticles.init();
})(window, jQuery);