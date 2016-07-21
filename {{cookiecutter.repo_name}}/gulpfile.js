// Include Gulp
var gulp = require('gulp');

// Plugins
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var autoprefixer = require('autoprefixer');
var postcss = require('gulp-postcss');
var cssnano = require('gulp-cssnano');

// Compile Sass from main.scss
gulp.task('sass', function() {
    return gulp.src('static/scss/main.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(cssnano())
        .pipe(gulp.dest('static/css'));
});

// Concatenate
gulp.task('scripts', function() {
    return gulp.src('static/js/*.js')
        .pipe(concat('all.js'))
        .pipe(gulp.dest('static/js'));
});

// PostCSS processor
gulp.task('css', function () {
    var processors = [
        autoprefixer({browsers: ['last 1 version']}),
    ];
    return gulp.src('static/css/*.css')
        .pipe(postcss(processors))
        .pipe(gulp.dest('static/css'))
});

// Watch files for changes
gulp.task('watch', function() { 
    gulp.watch('static/js/*.js', ['scripts']);
    gulp.watch('static/scss/*.scss', ['sass']);
    gulp.watch('static/css/*.css', ['css']);
});

// Default Task
gulp.task('default', ['sass', 'css', 'scripts', 'watch']);
