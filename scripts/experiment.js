// customize the experiment by specifying a view order and a trial structure
exp.customize = function() {
    // record current date and time in global_data
    this.global_data.startDate = Date();
    this.global_data.startTime = Date.now();
    // specify view order
    this.views_seq = [
        intro,
        botcaptcha,
        instruction_screen,
        main,
        postTest,
        thanks
    ];

    imageSeenBefore = [];

    main_trials = _.shuffle(main_trials)[0]

    health = [];

    for (let i = 0; i < main_trials.length; i++) {
        if (main_trials[i]['category'] == 'health') {
            health.push(main_trials[i])
        }
    }

    health = _.sampleSize(health, 1);

    imageSeenBefore.push(health[0]['filename']);

//    console.log("image seen before ", imageSeenBefore)

//    console.log("Health ", health)

    news_journals = [];

    for (let i = 0; i < main_trials.length; i++) {
        if (main_trials[i]['category'] == 'news' && !imageSeenBefore.includes(main_trials[i]['filename'])) {
            news_journals.push(main_trials[i])
        }
    }

//    console.log("News journals ", news_journals)

    news_journals = _.sampleSize(news_journals, 1);

    imageSeenBefore.push(news_journals[0]['filename']);

//    console.log("news journals ", news_journals)

    science_journals = [];

    for (let i = 0; i < main_trials.length; i++) {
        if (main_trials[i]['category'] == 'science_journals' && !imageSeenBefore.includes(main_trials[i]['filename'])) {
            science_journals.push(main_trials[i])
        }
    }

//    console.log("Science journals ", science_journals)

    science_journals = _.sampleSize(science_journals, 1);
    imageSeenBefore.push(science_journals[0]['filename']);

    travel = [];

    for (let i = 0; i < main_trials.length; i++) {
        if (main_trials[i]['category'] == 'travel' && !imageSeenBefore.includes(main_trials[i]['filename'])) {
            travel.push(main_trials[i])
        }
    }

//    console.log("travel ", travel)

    travel = _.sampleSize(travel, 1);

    imageSeenBefore.push(travel[0]['filename']);

    shopping = [];

    for (let i = 0; i < main_trials.length; i++) {
        if (main_trials[i]['category'] == 'shopping' && !imageSeenBefore.includes(main_trials[i]['filename'])) {
            shopping.push(main_trials[i])
        }
    }

//    console.log("shopping ", shopping)

    shopping = _.sampleSize(shopping, 1);

    imageSeenBefore.push(shopping[0]['filename']);

    social_media = [];

    for (let i = 0; i < main_trials.length; i++) {
        if (main_trials[i]['category'] == 'social_media' && !imageSeenBefore.includes(main_trials[i]['filename'])) {
            social_media.push(main_trials[i])
        }
    }

    social_media = _.sampleSize(social_media, 1);
//    console.log('social_media chosen ', social_media)    

    main_trials.length = 0
    main_trials.push(...health)
    main_trials.push(...news_journals)
    main_trials.push(...science_journals)
    main_trials.push(...travel)
    main_trials.push(...shopping)
    main_trials.push(...social_media)


    // randomize main trial order, but keep practice trial order fixed
    this.trial_info.main_trials = _.shuffle(main_trials);
    console.log("Number of stimuli");
    console.log(main_trials.length);
    console.log(this.trial_info.main_trials);

    // sample question order
    shopping = "Why did this image appear within this context?"
    travel = "You are browsing a <strong> travel website</strong>, with the goal of traveling to a new location."
    social_media = "You are browsing <strong> social media</strong>, with the goal of learning more about your connections."
    health = "You are browsing a <strong> health website</strong>, with the goal of learning how to live a healthier lifestyle."
    science_journals = "You are browsing <strong>science magazines</strong> (such as National Geographic), with the goal of learning more about recent science developments."
    news_journals = "You are browsing <strong>news websites</strong> (such as New York Times), with the goal of learning more about recent news developments."

    questions = _.shuffle([health, shopping, travel, social_media, science_journals, news_journals])
    // adds progress bars to the views listed
    // view's name is the same as object's name
    this.progress_bar_in = ["main"];
    // this.progress_bar_in = ['practice', 'main'];
    // styles: chunks, separate or default
    this.progress_bar_style = "default";
    // the width of the progress bar or a single chunk
    this.progress_bar_width = 100;
};